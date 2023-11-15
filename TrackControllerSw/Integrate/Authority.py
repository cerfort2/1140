import Block
from Block import *
class Authority():
    self.route = []

    def __init__(self, blo):
        self.blocks = blo
        # trackModelAuthority.emit(first)

    
    def newRoute(rou):
        #Add a new route when train created
        self.route.append(rou)

    def calculate(self, num):
        #For every block that is occupied count the blocks to the next stop
        for i in range(len(self.blocks)):
            if(self.blocks[i].getOccupancy()):
                if(self.route[num][0][0] == self.blocks[i].getName()):
                    stop = self.route[num][1][0]
                    auth1 = 0
                    while(not stop):
                        auth1 = auth1 + 1
                        stop = self.route[num][1][auth1]
        #Triple redundancy
        for i in range(len(self.blocks)):
            if(self.blocks[i].getOccupancy()):
                if(self.route[num][0][0] == self.blocks[i].getName()):
                    stop = self.route[num][1][0]
                    auth2 = 0
                    while(not stop):
                        auth2 = auth2 + 1
                        stop = self.route[num][1][auth2]
        for i in range(len(self.blocks)):
            if(self.blocks[i].getOccupancy()):
                if(self.route[num][0][0] == self.blocks[i].getName()):
                    stop = self.route[num][1][0]
                    auth3 = 0
                    while(not stop):
                        auth3 = auth3 + 1
                        stop = self.route[num][1][auth3]
        #If authority is zero and not at a stop return null
        if(auth1 == 0 and not self.route[num][1][0]):
            return
        #Triple Redundancy
        if(auth1 == auth2):
            self.route[num][0].pop(0)
            self.route[num][1].pop(0)
            return auth1
        if(auth2 == auth3):
            self.route[num][0].pop(0)
            self.route[num][1].pop(0)
            return auth2
        if(auth1 == auth3):
            self.route[num][0].pop(0)
            self.route[num][1].pop(0)
            return aith1
        return
                        


    