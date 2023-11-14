import Block
from Block import *
class PLC():
    def __init__(self, blo:Block = []):
        self.blocks = blo

    def logic(self, auth:int):
        #D Switch
        #12 is D13
        #0 is A1
        if(self.blocks[12].getOccupancy()): 
            self.blocks[12].setSwitch(False)
        if(self.blocks[0].getOccupancy()):
            self.blocks[12].setSwitch(True)

        #G Switch
        #28 is G29
        #149 is Z150
        if(self.blocks[28].getOccupancy()):
            self.blocks[28].setSwitch(False)
        if(self.blocks[149].getOccupancy()):
            self.blocks[28].setSwitch(True)

        #To Yard Switch
        #57 is J58
        if(auth == 0):
            self.blocks[57].setSwitch(False)
        else:
            self.blocks[57].setSwitch(True)

        #From Yard Switch
        #60 is J61
        #61 is J62
        #150 is YARD
        if(self.blocks[60].getOccupancy()):
            self.blocks[61].setSwitch(False)
        if(self.blocks[150].getOccupancy()):
            self.blocks[61].setSwitch(True)

        #N Switch
        #75 is M76
        #76 is N77
        if(self.blocks[75].getOccupancy()):
            self.blocks[76].setSwitch(True)
        if(self.blocks[76].getOccupancy()):
            self.blocks[76].setSwitch(False)

        #O Switch
        #84 is N85
        #99 is Q100
        if(self.blocks[84].getOccupancy()):
            self.blocks[84].setSwitch(False)
        if(self.blocks[99].getOccupancy()):
            self.blocks[84].setSwitch(True)

        #Crossroad
        #18 is E19
        if(self.blocks[17].getOccupancy() or self.blocks[18].getOccupancy() or self.blocks[19].getOccupancy()):
            self.blocks[18].setCrossroad(True)
        else:
            self.blocks[18].setCrossroad(False)