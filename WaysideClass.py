from TrackClass import Track

class Wayside():
    def __init__(self):
        self.tracks = []
    
    def createTrack(self,switch:bool, crossroad:bool, light:bool, station:bool, right= "", left= ""): #Adding a new track to the list
        self.tracks.append(Track(switch, crossroad, light, station))
        if switch == True: #If it is a switch you can also specify the Left and Right Destination
            self.tracks[self.tracks.__len__()-1].setLeftDest(left)
            self.tracks[self.tracks.__len__()-1].setRightDest(right)
    
    def getTrack(self, index): #Gets a certain track from the Wayside
        return self.tracks[index]