import Wayside
from Wayside import *
import Block
from Block import *
class Track():
    side:Wayside = [Wayside("Green 1"), Wayside("Green 2"), Wayside("Green 3"), Wayside("Green 4")]
    side[0].addBlock(False, False, True, "A1") #Signal
    side[0].addBlock(False, False, False, "A2")
    side[0].addBlock(False, False, False, "A3")
    side[0].addBlock(False, False, False, "B4") 
    side[0].addBlock(False, False, False, "B5")
    side[0].addBlock(False, False, False, "B6")
    side[0].addBlock(False, False, False, "B7")
    side[0].addBlock(False, False, False, "B8")
    side[0].addBlock(False, False, False, "C9")
    side[0].addBlock(False, False, False, "C10")
    side[0].addBlock(False, False, False, "C11")
    side[0].addBlock(False, False, False, "C12") 
    side[0].addBlock(True, False, True, "D13", "C12", "A1") #Switch, Signal
    side[0].addBlock(False, False, False, "D14")
    side[0].addBlock(False, False, False, "D15")
    side[0].addBlock(False, False, False, "D16")
    side[0].addBlock(False, False, False, "E17")
    side[0].addBlock(False, False, False, "E18")
    side[0].addBlock(False, True, False, "E19") #Crossroad
    side[0].addBlock(False, False, False, "E20") 
    side[0].addBlock(False, False, False, "F21") 
    side[0].addBlock(False, False, False, "F22")
    side[0].addBlock(False, False, False, "F23") 
    side[0].addBlock(False, False, False, "F24")
    side[0].addBlock(False, False, False, "F25") 
    side[0].addBlock(False, False, False, "F26")
    side[0].addBlock(False, False, False, "F27")
    side[0].addBlock(False, False, False, "F28")
    side[0].addBlock(True, False, True, "G29", "G30", "Z150") #Switch, Signal
    side[0].addBlock(False, False, False, "G30")
    side[0].addBlock(False, False, False, "G31")
    side[0].addBlock(False, False, False, "G32")
    side[1].addBlock(False, False, False, "H33")
    side[1].addBlock(False, False, False, "H34")
    side[1].addBlock(False, False, False, "H35")
    side[1].addBlock(False, False, False, "I36")
    side[1].addBlock(False, False, False, "I37")
    side[1].addBlock(False, False, False, "I38")
    side[1].addBlock(False, False, False, "I39")
    side[1].addBlock(False, False, False, "I40")
    side[1].addBlock(False, False, False, "I41") 
    side[1].addBlock(False, False, False, "I42")
    side[1].addBlock(False, False, False, "I43")
    side[1].addBlock(False, False, False, "I44")
    side[1].addBlock(False, False, False, "I45")
    side[1].addBlock(False, False, False, "I46")
    side[1].addBlock(False, False, False, "I47")
    side[1].addBlock(False, False, False, "I48") #Station
    side[1].addBlock(False, False, False, "I49")
    side[1].addBlock(False, False, False, "I50")
    side[1].addBlock(False, False, False, "I51")
    side[1].addBlock(False, False, False, "I52")
    side[1].addBlock(False, False, False, "I53")
    side[1].addBlock(False, False, False, "I54") 
    side[1].addBlock(False, False, False, "I55")
    side[1].addBlock(False, False, False, "I56")
    side[1].addBlock(False, False, False, "I57")
    side[1].addBlock(True, False, True, "J58", "YARD", "J59") #Switch, Signal
    side[1].addBlock(False, False, False, "J59")
    side[1].addBlock(False, False, False, "J60")
    side[1].addBlock(False, False, True, "J61") #Signal
    side[1].addBlock(True, False, False, "J62", "J61", "YARD") #switch
    side[1].addBlock(False, False, False, "K63")
    side[1].addBlock(False, False, False, "K64")
    side[1].addBlock(False, False, False, "K65")
    side[1].addBlock(False, False, False, "K66")
    side[1].addBlock(False, False, False, "K67")
    side[1].addBlock(False, False, False, "K68")
    side[1].addBlock(False, False, False, "L69")
    side[1].addBlock(False, False, False, "L70")
    side[1].addBlock(False, False, False, "L71")
    side[1].addBlock(False, False, False, "L72")
    side[1].addBlock(False, False, False, "L73")
    side[2].addBlock(False, False, False, "M74")
    side[2].addBlock(False, False, False, "M75")
    side[2].addBlock(False, False, True, "M76") #Signal
    side[2].addBlock(True, False, True, "N77", "R101", "M76") #Switch, Signal
    side[2].addBlock(False, False, False,"N78")
    side[2].addBlock(False, False, False,"N79")
    side[2].addBlock(False, False, False,"N80")
    side[2].addBlock(False, False, False,"N81")
    side[2].addBlock(False, False, False, "N82")
    side[2].addBlock(False, False, False, "N83")
    side[2].addBlock(False, False, False, "N84")
    side[2].addBlock(True, False, True, "N85", "O86", "Q100") #Switch, Signal
    side[2].addBlock(False, False, False, "O86")
    side[2].addBlock(False, False, False, "O87")
    side[2].addBlock(False, False, False, "O88") #Station
    side[2].addBlock(False, False, False, "P89")
    side[2].addBlock(False, False, False, "P90")
    side[2].addBlock(False, False, False, "P91")
    side[2].addBlock(False, False, False, "P92")
    side[2].addBlock(False, False, False, "P93")
    side[2].addBlock(False, False, False, "P94")
    side[2].addBlock(False, False, False, "P95")
    side[2].addBlock(False, False, False, "P96")
    side[2].addBlock(False, False, False, "P97")
    side[2].addBlock(False, False, False, "Q98")
    side[2].addBlock(False, False, False, "Q99")
    side[2].addBlock(False, False, True, "Q100") #Signal
    side[2].addBlock(False, False, False, "R101")
    side[3].addBlock(False, False, False, "S102")
    side[3].addBlock(False, False, False, "S103")
    side[3].addBlock(False, False, False, "S104")
    side[3].addBlock(False, False, False, "T105")
    side[3].addBlock(False, False, False, "T106")
    side[3].addBlock(False, False, False, "T107")
    side[3].addBlock(False, False, False, "T108")
    side[3].addBlock(False, False, False, "T109")
    side[3].addBlock(False, False, False, "U110")
    side[3].addBlock(False, False, False, "U111")
    side[3].addBlock(False, False, False, "U112")
    side[3].addBlock(False, False, False, "U113")
    side[3].addBlock(False, False, False, "U114")
    side[3].addBlock(False, False, False, "U115")
    side[3].addBlock(False, False, False, "U116")
    side[3].addBlock(False, False, False, "V117")
    side[3].addBlock(False, False, False, "V118")
    side[3].addBlock(False, False, False, "V119")
    side[3].addBlock(False, False, False, "V120")
    side[3].addBlock(False, False, False, "V121")
    side[3].addBlock(False, False, False, "W122")
    side[3].addBlock(False, False, False, "W123")
    side[3].addBlock(False, False, False, "W124")
    side[3].addBlock(False, False, False, "W125")
    side[3].addBlock(False, False, False, "W126")
    side[3].addBlock(False, False, False, "W127")
    side[3].addBlock(False, False, False, "W128")
    side[3].addBlock(False, False, False, "W129")
    side[3].addBlock(False, False, False, "W130")
    side[3].addBlock(False, False, False, "W131")
    side[3].addBlock(False, False, False, "W132")
    side[3].addBlock(False, False, False, "W133")
    side[3].addBlock(False, False, False, "W134")
    side[3].addBlock(False, False, False, "W135")
    side[3].addBlock(False, False, False, "W136")
    side[3].addBlock(False, False, False, "W137")
    side[3].addBlock(False, False, False, "W138")
    side[3].addBlock(False, False, False, "W139")
    side[3].addBlock(False, False, False, "W140")
    side[3].addBlock(False, False, False, "W141")
    side[3].addBlock(False, False, False, "W142")
    side[3].addBlock(False, False, False, "W143")
    side[3].addBlock(False, False, False, "X144")
    side[3].addBlock(False, False, False, "X145")
    side[3].addBlock(False, False, False, "X146")
    side[3].addBlock(False, False, False, "Y147")
    side[3].addBlock(False, False, False, "Y148")
    side[3].addBlock(False, False, False, "Y149")
    side[0].addBlock(False, False, True, "Z150") #Signal
    side[1].addBlock(False, False, False, "Z151")


    def __init__(self):
        #Create a list of track blocks from data given
        self.blocks:Block = []

    def setRoute(self, travel):
        self.route = travel
        

    def create(self,data):
        #TESTING
        for i in range (len(self.side)):
            for j in range (len(self.side[i].blocks)):
                self.blocks.append(self.side[i].getBlock(j))

        for i in range (len(self.blocks)):
            for j in range (len(self.blocks)):
                if(self.blocks[i].getName() < self.blocks[j].getName()):
                    temp = self.blocks[i]
                    self.blocks[i] = self.blocks[j]
                    self.blocks[j] =temp


        # for i in range (len(data[0])):
        #     self.blocks.append(Block(data[0][i], data[1][i], data[2][i], data[3][i])) #hasSwitch, hasCrossroad, hasSignal, name
        #     if(data[0][i]):
        #         self.blocks[i].setLeft(data[4][i]) #left
        #         self.blocks[i].setRight(data[5][i]) #right
        
        # #Seperate Blocks into designated wayside
        # self.waysides:Wayside = [Wayside("Green1"), Wayside("Green2"), Wayside("Green3"), Wayside("Green4")]
        # for i in range (len(self.blocks)):
        #     if(i <= 31 or i == 149):
        #         self.waysides[0].add(self.blocks[i])
        #     elif(i <= 72 or i == 150):
        #         self.waysides[1].add(self.blocks[i])
        #     elif(i <= 100):
        #         self.waysides[2].add(self.blocks[i])
        #     else:
        #         self.waysides[3].add(self.blocks[i])

        return self.side

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
        #trackModelData.emit(data)
    
    def getOccupancy(self):
        #Created lists
        data = []
        #Create a list of block names
        for i in range (len(self.blocks)):
            if(self.blocks[i].getOccupancy()):
                data.append(self.blocks[i].getName())
        #Return data
        return data

    def setOccupancy(self, data:bool = []):
        #Insert Occupancy
        for i in range (len(data)):
            self.blocks[i].setOccupancy(data[i])

        
