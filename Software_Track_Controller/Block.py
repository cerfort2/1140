class Block():
    

    #Default setup
    def __init__(self, switch:bool, crossroad:bool, signal:bool, tag:str):
        #Class Variables
        self.hasSwitch:bool = switch #If block has a switch
        self.switchStatus:bool = False #False if left True if right
        self.leftBlock:str = "" #Name of left block
        self.rightBlock:str = "" #Name of right block

        self.hasCrossroad:bool = crossroad #If block has a crossroad
        self.crossroadStatus:bool = False #False if crossroad open True if crossroad closed

        self.hasSignal:bool = signal #Has signal only when has switch
        self.signalStatus:bool = True #True if red False if green

        self.occupancy:bool = False #If block is occupied

        self.name:str = tag #Block name

    #Returns if block has a switch
    def getHasSwitch(self):
        return self.hasSwitch
    
    #Returns if block has a crossroad
    def getHasCrossroad(self):
        return self.hasCrossroad
    
    #Returns if block has a signal
    def getHasSignal(self):
        return self.hasSignal
    
    #Returns switch value if has a switch
    def getSwitch(self):
        if(self.hasSwitch):
            return self.switchStatus
        else:
            print("No switch")
    
    #Returns crossroad value if has a crossroad
    def getCrossroad(self):
        if(self.hasCrossroad):
            return self.crossroadStatus
        else:
            print("No crossroad")

    #Returns signal value if has a signal
    def getSignal(self):
        if(self.hasSignal):
            return self.signalStatus
        else:
            print("No signal")

    #Returns occupancy of block
    def getOccupancy(self):
        return self.occupancy
    
    #Returns left block if has a switch
    def getLeft(self):
        if(self.hasSwitch):
            return self.leftBlock
        else:
            print("No switch")
    
    #Returns right block if has a switch
    def getRight(self):
        if(self.hasSwitch):
            return self.rightBlock
        else:
            print("No switch")

    #Returns block name
    def getName(self):
        return self.name

    #Sets switch value if has a switch
    def setSwitch(self, set:bool):
        if(self.hasSwitch):
            self.switchStatus = set
        else:
            print("No switch")
    
    #Sets crossroad value if has a crossroad
    def setCrossroad(self, set:bool):
        if(self.hasCrossroad):
            self.crossroadStatus = set
        else:
            print("No crossroad")

    #Sets signal value if has a signal
    def setSignal(self, set:bool):
        if(self.hasSignal):
            self.signalStatus = set
        else:
            print("No signal")

    #Sets occupancy value
    def setOccupancy(self, set:bool):
        self.occupancy = set

    #Sets left block if has a switch
    def setLeft(self, left:str):
        if(self.hasSwitch):
            self.leftBlock = left
        else:
            print("No switch")
    
    #Sets right block if has a switch
    def setRight(self, right:str):
        if(self.hasSwitch):
            self.rightBlock = right
        else:
            print("No switch")
        
    #Sets the blocks name
    def setname(self, tag:str):
        self.name = tag
    


    


