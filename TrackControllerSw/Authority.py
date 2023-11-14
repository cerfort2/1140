import Block
from Block import *
class Authority():
    def __init__(travel, blo, first):
        self.route = travel
        self.blocks = blo
        trackModelAuthority.emit(first)

    
    def getRoute():
        #return route
        trackModelRoute.emit(route)

    def calculate():
        for i in range(len(self.blocks)):
            if(self.blocks[i].getOccupancy()):
                if(self.route[0][0] == self.blocks[i].getName()):
                    stop = self.route[1][0]
                    auth = 0
                    while(not stop):
                        auth = auth + 1
                        stop = self.route[1][auth]
                    self.route[0].pop(0)
                    self.route[1].pop(0)
                    #return auth
                    trackModelAuthority.emit(auth)
        #return null
        trackModelAuthority.emit()
                        


    