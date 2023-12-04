from Hardware_Track_Controller.TrackClass import Track

class Wayside():
    def __init__(self):
        self.tracks = []
    
    def createTrack(self,switch:bool, crossroad:bool, light:bool, trackName:str, left= "", right= ""): #Adding a new track to the list
        self.tracks.append(Track(switch, crossroad, light, trackName))
        if switch == True: #If it is a switch you can also specify the Left and Right Destination
            self.tracks[self.tracks.__len__()-1].setLeftDest(left)
            self.tracks[self.tracks.__len__()-1].setRightDest(right)
    
    def getTrack(self, index): #Gets a certain track from the Wayside
        return self.tracks[index]
    
    def getTrackName(self, index):
        return self.tracks[index].getTrackName()
    
    def amountOfTracks(self):
        return len(self.tracks)