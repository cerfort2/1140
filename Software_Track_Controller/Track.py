import Software_Track_Controller.Wayside
from Software_Track_Controller.Wayside import *
import Software_Track_Controller.Block
from Software_Track_Controller.Block import *
from Software_Track_Controller.SwTrackControlSetup import *
class Track():

    def __init__(self):
        #Create a list of track blocks from data given
        self.blocks:Block = []
    

    def create(self,data):

        for i in range (len(data[0])):
            self.blocks.append(Block(data[0][i], data[1][i], data[2][i], data[3][i])) #hasSwitch, hasCrossroad, hasSignal, name
            if(data[0][i]):
                self.blocks[i].setLeft(data[4][i]) #left
                self.blocks[i].setRight(data[5][i]) #right
        
        #Seperate Blocks into designated wayside
        if(len(self.blocks) == 151):
            self.waysides:Wayside = [Wayside("Green1"), Wayside("Green2"), Wayside("Green3"), Wayside("Green4")]
            for i in range (len(self.blocks)):
                if(i <= 31 or i == 149):
                    self.waysides[0].add(self.blocks[i])
                elif(i <= 72 or i == 150):
                    self.waysides[1].add(self.blocks[i])
                elif(i <= 100):
                    self.waysides[2].add(self.blocks[i])
                else:
                    self.waysides[3].add(self.blocks[i])
        else:
            self.waysides:Wayside = [Wayside("Red1"), Wayside("Red2")]
            for i in range (len(self.blocks)):
                if(i < 35 or i >= 71):
                    self.waysides[0].add(self.blocks[i])
                else:
                    self.waysides[1].add(self.blocks[i])
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
        return data

    
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
        return data

    def setOccupancy(self, data:bool = []):
        for i in range (len(data)):
            self.blocks[i].setOccupancy(data[i])

        
