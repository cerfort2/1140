import Wayside
from Wayside import *
import Block
from Block import *
class Track():
    waysides:Wayside = []
    blocks:Block = []

    def __init__(self, ways:Wayside = []):
        self.waysides = ways
        self.blocks:Block = []
        #Create list of blocks from waysides
        for i in range (len(self.waysides)):
            for j in range (len(self.waysides[i].blocks)):
                self.blocks.append(self.waysides[i].getBlock(j))
        #Sort list of blocks
        for i in range (len(self.blocks)):
            for j in range (i, len(self.blocks)):
                if(self.blocks[i].name > self.blocks[j].name):
                    hold = self.blocks[i]
                    self.blocks[i] = self.blocks[j]
                    self.blocks[j] = hold
 
    def getData(self):
        #Created lists
        data = [[],[],[]]
        
        #Create data array
        for i in range (len(self.blocks)):
            if(self.blocks[i].getHasSwitch()):
                data[0].append(self.blocks[i].getSwitch())
            else:
                data[0].append(False)
            if(self.blocks[i].getHasCrossroad()):
                data[1].append(self.blocks[i].getCrossroad())
            else:
                data[1].append(False)  
            if(self.blocks[i].getHasSignal()):
                data[2].append(self.blocks[i].getSignal())
            else:
                data[2].append(False) 
        #Return data
        return data
    
    def getOccupancy(self):
        #Created lists
        data = []
        #Create a list of block names
        for i in range (len(self.blocks)):
            if(self.blocks[i].getOccupancy()):
                data.append(self.blocks[i].name)
        #Return data
        return data

    def setOccupancy(self, data:bool = []):
        #Insert Occupancy
        for i in range (len(self.blocks)):
            self.blocks[i].setOccupancy(data[i])
