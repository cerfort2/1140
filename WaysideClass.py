from TrackClass import Track

class Wayside():
    def __init__(self):
        self.tracks = []
    
    def createTrack(self,switch, crossroad, light):
        self.tracks.append(Track(switch, crossroad, light))