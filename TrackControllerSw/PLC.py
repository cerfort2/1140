import Block
from Block import *
class PLC():

    def logic(self, auth:int, blocks:Block):
        #D Switch
        #12 is D13
        #0 is A1
        if(blocks[12].getOccupancy()): 
            blocks[12].setSwitch(False)
        if(blocks[0].getOccupancy()):
            blocks[12].setSwitch(True)

        #G Switch
        #28 is G29
        #149 is Z150
        if(blocks[28].getOccupancy()):
            blocks[28].setSwitch(False)
        if(blocks[149].getOccupancy()):
            blocks[28].setSwitch(True)

        #To Yard Switch
        #57 is J58
        if(auth == 0):
            blocks[57].setSwitch(False)
        else:
            blocks[57].setSwitch(True)

        #From Yard Switch
        #60 is J61
        #61 is J62
        #150 is YARD
        if(blocks[60].getOccupancy()):
            blocks[61].setSwitch(False)
        if(blocks[150].getOccupancy()):
            blocks[61].setSwitch(True)

        #N Switch
        #75 is M76
        #76 is N77
        if(blocks[75].getOccupancy()):
            blocks[76].setSwitch(True)
        if(blocks[76].getOccupancy()):
            blocks[76].setSwitch(False)

        #O Switch
        #84 is N85
        #99 is Q100
        if(blocks[84].getOccupancy()):
            blocks[84].setSwitch(False)
        if(blocks[99].getOccupancy()):
            blocks[84].setSwitch(True)

        #Crossroad
        #18 is E19
        if(blocks[17].getOccupancy() or blocks[18].getOccupancy() or blocks[19].getOccupancy()):
            blocks[18].setCrossroad(True)
        else:
            blocks[18].setCrossroad(False)