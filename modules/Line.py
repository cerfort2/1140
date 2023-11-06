from datetime import datetime, timedelta, date
from Block import Block
import pandas as pd

class Line():
    def __init__(self, file):
        super().__init__()
        self.blocks = self.read_data(filePath = 'Green Line Info.xlsx')
        
    
    def read_data(self, filePath):
        
        df = pd.read_excel(filePath)
        blocks_list = []
        

        for index, row in df.iterrows():
            station = None
            switch = False
            underground = False
            if pd.notna(row['Infrastructure']):
            # Split the infrastructure data into components
                infra_components = row['Infrastructure'].split(';')
                
                station = None
                has_stations = []
                switch = False
                underground = False
                # Parse each component
                for component in infra_components:
                    component = component.strip()  # Remove any leading/trailing whitespace
                    if 'STATION' in component:
                        station = component.replace('STATION:', '').strip()  # Get the station name
                        has_stations.append(True)
                    else:
                        station = "0"
                        has_stations.append(False)
                    if 'SWITCH' in component:
                        switch = True
                    if 'UNDERGROUND' in component or 'UNDERDROUND' in component:  # Handling a typo
                        underground = True
            self.has_stations = has_stations
            self.sections = df['Section'].tolist()
            self.block_num = df['Block Number'].tolist()
            self.block_lengths = df['Block Length (m)'].tolist()
            self.speed_limits = df['Speed Limit (Km/Hr)'].tolist()

            # Create a new Block object with the parsed data and append it to the list
            block = Block(
                section=row['Section'],
                number=row['Block Number'],
                length=row['Block Length (m)'],
                spd_lim=row['Speed Limit (Km/Hr)'],
                station=station,
                dwell=0,  # Assuming default dwell time is 0, since it's not provided
                has_switch=switch,
                is_underground=underground
            )
            blocks_list.append(block)

        return blocks_list

    #returns the route from yard given an input station
    def get_route(self, station):
        return
    #returns a suggested velocity for each block given the route
    def get_velocities(self, blocK_list):
        return
    #returns the authority from the yard given an input station  
    def get_authority(self, station):
        authority_sum = 0
        for block in self.blocks:
            authority_sum += block.get_length()

            if block.get_station() == station:
                break
    
        return authority_sum
    
    #returns the route from yard given a list of input stations
    def get_routes(self, station_list):
        route_blocks = []
        stop_or_dest = []
        for block in self.blocks:
            route_blocks.append(block)
            if block.station in station_list:
                stop_or_dest.append(True)
                if block.station == station_list[-1]:
                    break
            else:
                stop_or_dest.append(False)
        return route_blocks, stop_or_dest
    #returns a list of suggested velocities for each block given a list of routes
    def get_velocities_mul(self, blocK_list_list):
        return
    #returns the authority from the yard given a list of input stations
    def get_authorities(self, station_list):
        return
    
    #calculates departure time given the arrival station
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