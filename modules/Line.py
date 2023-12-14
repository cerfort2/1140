from datetime import datetime, timedelta, date
from modules.Block import Block
import pandas as pd
from scipy.optimize import minimize
import numpy as np

class Line():
    def __init__(self, name, file):
        super().__init__()
        self.blocks = self.read_data(file)
        self.name = name
        
    def read_data(self, filePath):
        df = pd.read_excel(filePath)
        blocks_list = []

        for index, row in df.iterrows():
            station = "0"  # Default value if no station is present
            switch = False
            underground = False

            if pd.notna(row['Infrastructure']):
                infra_components = row['Infrastructure'].split('\n')


                for component in infra_components:
                    component_cleaned = component.strip()
                    
                    if 'STATION' in component_cleaned:
                        station_name = component_cleaned.replace('STATION', '').replace('UNDERGROUND', '').replace(';', '').strip()
                        station = station_name if station_name else "0"    
                    if 'SWITCH' in component_cleaned:
                        switch = True
                        
                    if 'UNDERGROUND' in component_cleaned:
                        underground = True

            # Create a Block object with the parsed data
            block = Block(
                section=row['Section'],
                number=row['Block Number'],
                length=row['Block Length (m)'],
                spd_lim=row['Speed Limit (Km/Hr)'],
                station=station,  # This will have the cleaned station name
                dwell=0,  # Assuming default dwell time is 0, since it's not provided
                has_switch=switch,
                is_underground=underground
            )
            blocks_list.append(block)
        #self.has_stations = has_stations
        #self.sections = df['Section'].tolist()
        #self.block_num = df['Block Number'].tolist()
        #self.block_lengths = df['Block Length (m)'].tolist()
        #self.speed_limits = df['Speed Limit (Km/Hr)'].tolist()

        return blocks_list
    #returns the route from yard given an input station
    def get_route_for_velocity(self, station_list):
        route_blocks = []
        stop_or_dest = []
        
        for block in self.blocks:
            route_blocks.append(str(block.get_section())+str(block.get_number()))
            station_check = str(block.get_section())+str(block.get_number()) + ": " + str(block.get_station())
            
            if station_check in station_list:
                stop_or_dest.append(True)
                if station_check == station_list[-1]:
                    break
            else:
                stop_or_dest.append(False)
        return route_blocks, stop_or_dest
    #returns the route from yard given an input station
    def get_route(self, station_list):
        route_blocks = []
        stop_or_dest = []
        route_feet = []
        
        for block in self.blocks:
            this_block = str(block.get_section())+str(block.get_number())
            if this_block == "J58":
                route_blocks.append("Z151")
                stop_or_dest.append(False)
                break
            route_blocks.append(this_block)
            station_check = str(block.get_section())+str(block.get_number()) + ": " + str(block.get_station())
            route_feet.append(block.get_length())
            
            if station_check in station_list:
                stop_or_dest.append(True)
            else:
                stop_or_dest.append(False)
        return route_blocks, stop_or_dest, route_feet
    """
    def travel_time_objective(speeds, block_lengths, total_time):
        # Objective function to minimize: sum of squared differences in speeds + penalty for total time deviation
        time_diffs = np.diff(speeds) ** 2
        travel_times = block_lengths / speeds
        total_time_penalty = (total_time - np.sum(travel_times)) ** 2
        return np.sum(time_diffs) + total_time_penalty

    def speed_limit_constraint(speeds, block_speed_limits):
        # Constraint function: speeds must be less than or equal to block speed limits
        return block_speed_limits - speeds

    def get_velocities(self, block_list, departure_time, arrival_time):
        # Parse the times
        time1 = datetime.strptime(departure_time, '%H:%M:%S')
        time2 = datetime.strptime(arrival_time, '%H:%M:%S')
        
        # Calculate total elapsed time in seconds
        total_time = (time2 - time1).total_seconds()
        
        # Prepare the data for the optimizer
        block_lengths = np.array([block.get_length() for block in block_list])
        block_speed_limits = np.array([block.get_speed_limit() for block in block_list])
        
        # Initial guess for the speeds (could be the average of the speed limits)
        initial_speeds = block_speed_limits.mean() * np.ones(len(block_list))
        
        # Define the constraints (speed limits and total travel time)
        #constraints = [{'type': 'ineq', 'fun': speed_limit_constraint, 'args': (block_speed_limits,)}]
        # Run the optimization
        result = minimize(
            travel_time_objective,
            initial_speeds,
            args=(block_lengths, total_time),
            constraints=constraints,
            bounds=[(0, limit) for limit in block_speed_limits]  # Speeds must be non-negative
        )
        
        if result.success:
            # If the optimization was successful, use the optimized speeds
            return result.x
        else:
            # Handle the case where optimization failed
            raise ValueError("Optimization failed to find a feasible solution")
"""
    #returns a suggested velocity for each block given the route
    def get_velocities(self, block_list, departure_time, arrival_time, num_stops):
        #calculate suggested speed for each block, should be constant value except in special cases
        time1 = datetime.strptime(departure_time.toString(), '%H:%M:%S')
        time2 = datetime.strptime(arrival_time.toString(), '%H:%M:%S')
        total_dwell_time = num_stops
        moving_time = (time2-time1).total_seconds() - total_dwell_time
        total_length = 0
        suggested_speeds = []
        index = 0
        for i in range(len(block_list[1]) - 1, -1, -1):
                if block_list[1][i] == 1:
                    index = i
                    
        for i, block in enumerate(block_list):
            block_list_block = str(self.blocks[i].get_section()) + str(self.blocks[i].get_number())

            if block_list_block == block:
                total_length += self.blocks[i].get_length()
                
            #suggested_speeds.append(5)
        speed_initial = total_length/moving_time
        for i in range(len(block_list)):
            suggested_speeds.append(speed_initial)

        return suggested_speeds

    def get_authority(self, stop_list):
        authorities = []
        cur_block_index = 0
        total_blocks = len(self.blocks)
        
        for stop in stop_list:
            print(stop)
            authority_sum = 0
            
            while cur_block_index < total_blocks:
                block = self.blocks[cur_block_index]
                station_check = str(block.get_section())+str(block.get_number())+": " +str(block.get_station())
                
                if station_check == stop:
                    authorities.append(authority_sum)
                    break
                
                authority_sum += block.get_length()  # Assuming each block contributes '1' to the authority
                cur_block_index += 1
                
        authority_sum = 0
        while cur_block_index < total_blocks:
            block = self.blocks[cur_block_index]
            if str(block.get_section())+str(block.get_number()) == "Z151":
                authorities.append(authority_sum)
            authority_sum+=self.blocks[cur_block_index].get_length()
            
            cur_block_index +=1
        return authorities

    #returns the route from yard given a list of input stations
    def get_routes(self, station_list_list):
        
        route_blocks = []
        stop_or_dest = []

        for block in self.blocks:
            route_blocks.append(block)

            if block.station in station_list_list:
                stop_or_dest.append(True)

                if block.station == station_list_list[-1]:
                    break
            else:
                stop_or_dest.append(False)
        return route_blocks, stop_or_dest
    
    #returns a list of suggested velocities for each block given a list of routes
    def get_velocities_mul(self, block_list_list):
        velocities_list = []
        for block_list in block_list_list:
            velocities_list.append(self.get_velocities(block_list))
        return velocities_list
    #returns the authority from the yard given a list of input stations
    def get_authorities(self, station_list):
        authorities_list = []
        for station in station_list:
            authorities_list.append(self.get_authority(station))
        return authorities_list
    
"""    #calculates departure time given the arrival station
    def calculate_dep_time(self, station, time):
        return
    
    #calculates departure times given the arrival station and time
    def calculate_dep_times(self, stations, times):
        return
    
    #calculates arrival time given the arrival time
    def calculate_arrival_time(self, station, time):
        
        delta = timedelta(hours = hrs, minutes = mins, seconds = secs)
        return delta
    
    #calculates arrival times given the arrival times and stations
    def calculate_arrival_times(self, stations, times):
        
        delta = timedelta(hours = hrs, minutes = mins, seconds = secs)
        return delta
"""