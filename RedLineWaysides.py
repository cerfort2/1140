from WaysideClass import Wayside

class RedLine():

    Waysides = [Wayside(), Wayside()] #All The waysides going in order of 1,2,3,4 for Green Line

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
            if(i <= 34 or 70 < i <= 75): #Create all tracks for Wayside 1
                self.Waysides[0].createTrack(switch[i], crossroad[i], light[i], trackName[i], left[i], right[i])
            if(34 < i <= 70): #Creates all tracks for Wayside 2
                self.Waysides[1].createTrack(switch[i], crossroad[i], light[i], trackName[i], left[i], right[i])