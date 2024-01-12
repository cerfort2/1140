from Hardware_Track_Controller.WaysideClass import Wayside

class RedLine():

    Waysides = [Wayside()] #All The waysides going in order of 1,2,3,4 for Green Line

    def setTracks(self, tracks): #Sets the Red Line tracks on setup of the track model
        switch = []
        crossroad = []
        light =[]
        trackName = []
        left = []
        right = []
        for i in range(len(tracks[0])):
            switch.append(tracks[0][i])
        for i in range(len(tracks[1])):
            crossroad.append(tracks[1][i])
        for i in range(len(tracks[2])):
            light.append(tracks[2][i])
        for i in range(len(tracks[3])):
            trackName.append(tracks[3][i])
        for i in range(len(tracks[4])):
            left.append(tracks[4][i])
        for i in range(len(tracks[5])):
            right.append(tracks[5][i])
        
        for i in range(len(tracks[0])):
            self.Waysides[0].createTrack(switch[i], crossroad[i], light[i], trackName[i], left[i], right[i])