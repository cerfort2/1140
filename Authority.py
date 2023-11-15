from TrackClass import Track

class AuthorityClass():
    route = []

    def init(self, blo):
        self.blocks = blo

    def setNewTrain(self, travel:[]):
        self.route.append(travel)

    def calculate(self, num):
        for i in range(len(self.blocks)):
            if(self.blocks[i].getOccupancy()):
                if(self.route[num][0][0] == self.blocks[i].getName()):
                    stop = self.route[num][1][0]
                    auth = 0
                    while(not stop):
                        auth = auth + 1
                        stop = self.route[num][1][auth]
                    self.route[num][0].pop(0)
                    self.route[num][1].pop(0)
                    return auth
        return 