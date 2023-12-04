import Block
from Block import *
class PLC():
    auth = 0
    def __init__(self, blo:Block = []):
        self.blocks = blo

    def setAuth(self, authin:int):
        self.auth = authin

    def logic(self):
        stoppage = []
        loop1 = False
        loop2 = False
        for i in range(0, 29):
            loop1 = loop1 or self.blocks[i].getOccupancy()
        for i in range(76, 100):
            loop2 = loop2 or self.blocks[i].getOccupancy()

        #Switch D13 - C12 , D13 - A1
        if(self.blocks[13].getOccupancy()): 
            self.blocks[12].setSwitch(False)
        if(self.blocks[0].getOccupancy()):
            self.blocks[12].setSwitch(True)
        #Signal A1
        if(self.blocks[0].getOccupancy()):
            self.blocks[0].setSignal(True)
        else:
            self.blocks[0].setSignal(False)
        #Signal D13
        if(self.blocks[13].getOccupancy()):
            self.blocks[12].setSignal(True)
        else:
            self.blocks[12].setSignal(False)

        #Crossroad E19
        if(self.block[16].getOccupancy or self.blocks[17].getOccupancy() or self.blocks[18].getOccupancy() or self.blocks[19].getOccupancy() or self.blocks[20].getOccupancy()):
            self.blocks[18].setCrossroad(True)
        else:
            self.blocks[18].setCrossroad(False)

        #Switch G29 - G30 , G29 - Z150
        if(self.blocks[27].getOccupancy()):
            self.blocks[28].setSwitch(False)
        elif(self.blocks[149].getOccupancy()):
            self.blocks[28].setSwitch(True)
        #Signal G29
        if(self.blocks[28].getOccupancy() and (self.blocks[29].getOccupancy() or self.blocks[30].getOccupancy())):
            stoppage.append(self.blocks[28].getName)
        if(self.blocks[28].getOccupancy() and not (self.blocks[29].getOccupancy() or self.blocks[30].getOccupancy())):
            self.blocks[28].setSignal(True)
        else:
            self.blocks[28].setSignal(False)
        #Signal Z150
        if(self.blocks[149].getOccupancy() and loop1):
            stoppage.append(self.blocks[149].getName)
        if(self.blocks[149].getOccupancy() and not loop1):
            self.blocks[149].setSignal(True)
        else:
            self.blocks[149].setSignal(False)
        
        #G30 -> M75
        for i in range(29, 75):
            if(self.blocks[i].getOccupancy()):
                if(self.blocks[i+1].getOccupancy() or self.blocks[i+2].getOccupancy()):
                    stoppage.append(self.blocks[i].getName())

        #Switch J58 - Yard , J58 - J59
        if(self.auth == 0):
            self.blocks[57].setSwitch(False)
        else:
            self.blocks[57].setSwitch(True)
        #Signal J58
        if(self.blocks[57].getOccupancy() and (self.blocks[58].getOccupancy() or self.blocks[59].getOccupancy())):
            stoppage.append(self.blocks[57].getName())
        if(self.blocks[57].getOccupancy() and not (self.blocks[58].getOccupancy() or self.blocks[59].getOccupancy())):
            self.blocks[57].setSignal(True)
        else:
            self.blocks[57].setSignal(False)

        #Switch J62 - J61 , J62 - Yard
        if(self.blocks[150].getOccupancy()):
            self.blocks[61].setSwitch(True)
        elif(self.blocks[60].getOccupancy()):
            self.blocks[61].setSwitch(False)
        

        #Signal yard
        if(self.blocks[150].getOccupancy() and (self.blocks[61].getOccupancy() or self.blocks[62].getOccupancy())):
            stoppage.append(self.blocks[150].getName())
        if(self.blocks[150].getOccupancy() and not(self.blocks[61].getOccupancy() or self.blocks[62].getOccupancy())):
            self.blocks[150].setSignal(True)
        else:
            self.blocks[150].setSignal(False)
        #signal J61
        if(self.blocks[60].getOccupancy() and (self.blocks[61].getOccupancy() or self.blocks[62].getOccupancy() or self.blocks[150].getOccupancy())):
            stoppage.append(self.blocks[60].getName())
        if(self.blocks[60].getOccupancy() and not(self.blocks[61].getOccupancy() or self.blocks[62].getOccupancy() or self.blocks[150].getOccupancy())):
            self.blocks[60].setSignal(True)
        else:
            self.blocks[60].setSignal(False)

            
        #Switch N77 - R101 , N77 - M76
        if(self.blocks[77].getOccupancy()):
            self.blocks[76].setSwitch(False)
        elif(self.blocks[75].getOccupancy()):
            self.blocks[76].setSwitch(True)
        
        #Signal M76
        if(self.blocks[75].getOccupancy() and loop2):
            stoppage.append(self.blocks[75].getName())
        if(self.blocks[75].getOccupancy() and not loop2):
            self.blocks[75].setSignal(True)
        else:
            self.blocks[75].setSignal(False)
        #signal N77
        if(self.blocks[76].getOccupancy() and (self.blocks[100].getOccupancy() or self.blocks[101].getOccupancy())):
            stoppage.append(self.blocks[76].getName())
        if(self.blocks[76].getOccupancy() and not (self.blocks[100].getOccupancy() or self.blocks[101].getOccupancy())):
            self.blocks[76].setSignal(True)
        else:
            self.blocks[76].setSignal(False)

        #Switch N85 - O86 , N85 - Q100
        if(self.blocks[83].getOccupancy()):
            self.blocks[84].setSwitch(False)
        if(self.blocks[99].getOccupancy()):
            self.blocks[84].setSwitch(True)
        #Signal N85
        if(self.blocks[84].getOccupancy()):
            self.blocks[84].setSignal(True)
        else:
            self.blocks[84].setSignal(False)
        #Signal Q100
        if(self.blocks[99].getOccupancy()):
            self.blocks[99].setSignal(True)
        else:
            self.blocks[99].setSignal(False)

        #R101 -> Y148
        for i in range(100, 148):
            if(self.blocks[i].getOccupancy()):
                if(self.blocks[i+1].getOccupancy() or self.blocks[i+2].getOccupancy()):
                    stoppage.append(self.blocks[i].getName())

        return stoppage


