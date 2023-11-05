

class Block():
    def __init__(self, section, number, length, spd_lim, station, dwell, has_switch, is_underground):
        super().__init__()
        self.section = section
        self.number = number
        self.length = length
        self.speed_limit = spd_lim
        self.station = station
        self.dwell_time = dwell
        self.switch = has_switch
        self.underground = is_underground