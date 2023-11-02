from datetime import datetime, timedelta, date


class Line():
    def __init__(self, name, speeds, blocks, block_lengths, station_list, times):
        super().__init__()
        self.suggested_speeds = speeds
        self.blocks = blocks
        self.block_lengths = block_lengths
        self.stations = station_list
        self.line_name = name
        self.block_times = times
    
    #returns the route from yard given an input station
    def get_route(self, station):
        return
    #returns a suggested velocity for each block given the route
    def get_velocities(self, blocK_list):
        return
    #returns the authority from the yard given an input station  
    def get_authority(self, station):
        return
    
    #returns the route from yard given a list of input stations
    def get_routes(self, station_list):
        return
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