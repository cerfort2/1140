import Software_Track_Controller.Block
from Software_Track_Controller.Block import *
class Authority():
    route = []

    def __init__(self, blo):
        self.blocks = blo
        # trackModelAuthority.emit(first)

    def newRoute(self, rou):
        #Add a new route when train created
        self.route.append(rou)

    def calculate(self, num):
        #For every block that is occupied count the blocks to the next stop
        if(len(self.route[num][0]) == 0):
            return
        for i in range(len(self.blocks)):
            if(self.blocks[i].getOccupancy()):
                if(self.route[num][0][0] == self.blocks[i].getName()):
                    stop = self.route[num][1][0]
                    auth1 = 0
                    while(not stop):
                        auth1 = auth1 + 1
                        stop = self.route[num][1][auth1]
                    stop = self.route[num][1][0]
                    auth2 = 0
                    while(not stop):
                        auth2 = auth2 + 1
                        stop = self.route[num][1][auth2]
                    stop = self.route[num][1][0]
                    auth3 = 0
                    while(not stop):
                        auth3 = auth3 + 1
                        stop = self.route[num][1][auth3]
                    if(auth1 == 0 and self.route[num][1][0] and len(self.route[num][0]) != 1):
                        self.route[num][1][0] = False
                    else:
                        self.route[num][0].pop(0)
                        self.route[num][1].pop(0)
                    if(auth1 == auth2):
                        return auth1
                    if(auth1 == auth3):
                        return auth1
                    if(auth2 == auth3):
                        return auth2
        return
                        


    