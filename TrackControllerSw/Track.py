import Wayside
from Wayside import *
import Block
from Block import *
class Track():

    def __init__(self):
        #Create a list of track blocks from data given
        self.blocks:Block = []

    def setRoute(self, travel):
        self.route = travel
        

    def create(self,data):

        for i in range (len(data[0])):
            self.blocks.append(Block(data[0][i], data[1][i], data[2][i], data[3][i])) #hasSwitch, hasCrossroad, hasSignal, name
            if(data[0][i]):
                self.blocks[i].setLeft(data[4][i]) #left
                self.blocks[i].setRight(data[5][i]) #right
        
        #Seperate Blocks into designated wayside
        self.waysides:Wayside = [Wayside("Green1"), Wayside("Green2"), Wayside("Green3"), Wayside("Green4")]
        for i in range (len(self.blocks)):
            if(i <= 31 or i == 149):
                self.waysides[0].append(self.blocks[i])
            elif(i <= 72 or i == 150):
                self.waysides[1].append(self.blocks[i])
            elif(i <= 100):
                self.waysides[2].append(self.blocks[i])
            else:
                self.waysides[3].append(self.blocks[i])

        return self.waysides

    def getBlocks(self):
        return self.blocks

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
        #return data
        trackModelData.emit(data)
    
    def getOccupied(self):
        #Created lists
        data = []
        #Create a list of block names
        for i in range (len(self.blocks)):
            if(self.blocks[i].getOccupancy()):
                data.append(self.blocks[i].getName())
        #Return data
        return data

    def getOccupancy(self):
        #Created lists
        data = []
        #Create a list of block names
        for i in range (len(self.blocks)):
                data.append(self.blocks[i].getOccupancy())
        #Return data
        ctcOccupancy.emit(data)

    def setOccupancy(self, data:bool = []):
        #Insert Occupancy
        for i in range (len(data)):
            self.blocks[i].setOccupancy(data[i])

        
