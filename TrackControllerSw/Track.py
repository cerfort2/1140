import Wayside
from Wayside import *
import Block
from Block import *
class Track():
    waysides:Wayside = []

    def __init__(self, ways:Wayside = []):
        self.waysides = ways
 
    def getData(self):
        #Created lists
        data = [[],[],[]]
        blocks:Block = []
        #Create list of blocks from waysides
        for i in range (len(self.waysides)):
            for j in range (len(self.waysides[i].blocks)):
                blocks.append(self.waysides[i].blocks[j])
        #Sort list of blocks
        for i in range (len(blocks)):
            for j in range (i, len(blocks)):
                if(blocks[i].name > blocks[j].name):
                    hold = blocks[i]
                    blocks[i] = blocks[j]
                    blocks[j] = hold
        hold = blocks[len(blocks) - 1]
        blocks[len(blocks) - 1] = blocks[len(blocks) - 2]
        blocks[len(blocks) - 2] = hold
        
        #Create data array
        for i in range (len(blocks)):
            if(blocks[i].getHasSwitch()):
                data[0].append(blocks[i].getSwitch())
            else:
                data[0].append(False)
            if(blocks[i].getHasCrossroad()):
                data[1].append(blocks[i].getCrossroad())
            else:
                data[1].append(False)  
            if(blocks[i].getHasSignal()):
                data[2].append(blocks[i].getSignal())
            else:
                data[2].append(False) 
        #Return data
        return data
    
    def getOccupancy(self):
        #Created lists
        data = []
        blocks:Block = []
        #Create list of blocks from waysides
        for i in range (len(self.waysides)):
            for j in range (len(self.waysides[i].blocks)):
                blocks.append(self.waysides[i].blocks[j])
        #Sort list of blocks
        for i in range (len(blocks)):
            for j in range (i, len(blocks)):
                if(blocks[i].name > blocks[j].name):
                    hold = blocks[i]
                    blocks[i] = blocks[j]
                    blocks[j] = hold
        hold = blocks[len(blocks) - 1]
        blocks[len(blocks) - 1] = blocks[len(blocks) - 2]
        blocks[len(blocks) - 2] = hold
        #Create a list of block names
        for i in range (len(blocks)):
            if(blocks[i].getOccupancy()):
                data.append(blocks[i].name)
        #Return data
        return data

    def setOccupancy(self, data:bool = []):
        #Create list
        blocks:Block = []
        #Create list of blocks from waysides
        for i in range (len(self.waysides)):
            for j in range (len(self.waysides[i].blocks)):
                blocks.append(self.waysides[i].blocks[j])
        #Sort list of blocks
        for i in range (len(blocks)):
            for j in range (i, len(blocks)):
                if(blocks[i].name > blocks[j].name):
                    hold = blocks[i]
                    blocks[i] = blocks[j]
                    blocks[j] = hold
        hold = blocks[len(blocks) - 1]
        blocks[len(blocks) - 1] = blocks[len(blocks) - 2]
        blocks[len(blocks) - 2] = hold
        #Insert Occupancy
        for i in range (len(blocks)):
            blocks[i].setOccupancy(data[i])
