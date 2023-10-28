class Block():
    #Class Variables
    hasSwitch:bool = False 
    switchStatus:bool = False #False if left True if right
    leftBlock:str = "" #Name of left block
    rightBlock:str = "" #Name of right block

    hasCrossroad:bool = False
    crossroadStatus:bool = False #False if crossroad open True if crossroad closed

    hasSignal:bool = False #Has signal only when has switch
    signalStatus:bool = False #False if green True if red

    hasStation:bool = False #Has station

    occupancy:bool = False #If block is occupied

    name:str = ""



    #Default setup
    def __init__(self, switch:bool, crossroad:bool, signal:bool, station:bool, tag:str):
        self.hasSwitch = switch
        self.hasCrossroad = crossroad
        self.hasSignal = signal
        self.hasStation = station
        self.name = tag

    def getHasSwitch(self):
        return self.hasSwitch
    
    def getHasCrossroad(self):
        return self.hasCrossroad
    
    def getHasSignal(self):
        return self.hasSignal
    
    def getHasStation(self):
        return self.hasStation
    
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
        
    


    


