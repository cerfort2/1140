class Block():
    def __init__(self, section, number, length, spd_lim, station=None, dwell=0, has_switch=False, is_underground=False):
        self.section = section
        self.number = number
        self.length = length
        self.speed_limit = spd_lim
        self.station = station
        self.switch = has_switch
        self.underground = is_underground
    
    #Setters
    def set_section(self, section):
        self.section = section
        
    def set_number(self, number):
        self.number = number
        
    def set_length(self, length):
        self.length = length
        
    def set_speed_limit(self, spd_lim):
        self.speed_limit = spd_lim
        
    def set_station(self, station):
        self.station = station
        
    def set_switch(self, has_switch):
        self.switch = has_switch
        
    def set_underground(self, is_underground):
        self.underground = is_underground
    
    #Getters
    def get_section(self):
        return self.section
        
    def get_number(self):
        return self.number
        
    def get_length(self):
        return self.length
        
    def get_speed_limit(self):
        return self.speed_limit
        
    def get_station(self):
        return self.station
        
    def get_switch(self):
        return self.switch
        
    def get_underground(self):
        return self.underground