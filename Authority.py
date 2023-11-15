from TrackClass import Track

class AuthorityClass():
    route = []

    def init(self, blo):
        self.blocks = blo

    def setNewTrain(self, travel, authStart, speed:[]):
        self.route.append(travel)
        self.firstAuthority = authStart
        self.suggestSpeed = speed

    def calculate(self):
        for i in range(len(self.blocks)):
            if(self.blocks[i].getOccupancy()):
                if(self.route[0][0] == self.blocks[i].getTrackName()):
                    stop = self.route[1][0]
                    auth = 0
                    while(not stop):
                        auth = auth + 1
                        stop = self.route[1][auth]
                    self.route[0].pop(0)
                    self.route[1].pop(0)
                    #return auth
                    return auth
        #return null
        return