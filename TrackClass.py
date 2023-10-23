class Track():
    #Class variables

    isCrossroad = False# #specify if Track has a crossroad
    crossroadStatus = False #False means up and True means down, default will be up

    occupancy = False #If occupied or not

    isLight = False #Specify if Track has a Light
    lightStatus = True #True is Red, False is Green

    #If it is a switch, input the destination tracks on left and right
    isSwitch = False
    rightDestination = ""
    leftDestination = ""
    switchStatus = True #Default switch to right(True = Right, False = left)

    isStation = False #Specify if the block is a station

    def __init__(self, switch:bool, crossroad:bool, light:bool, station:bool): #Initlize a Track to be set as a switch or a crossroad
        self.isSwitch = switch
        self.isLight = light
        self.isCrossroad = crossroad
        self.isStation = station
    
    def getOccupancy(self): #Get the occupancy
        return self.occupancy
    
    def setOccupancy(self, occu:bool): #Get the occupancy
        self.occupancy = occu
    
    def setRightDest(self, right): #Set the right destination if it is a switch, no need for get because value is static
        if self.isSwitch == True:
            self.rightDestination = right
        else:
            print("Track is not a Switch")
    
    def setLeftDest(self, left): #Set the left destination if it is a switch, no need for get because value is static
        if self.isSwitch == True:
            self.leftDestination = left
        else:
            print("Track is not a Switch")

    def setSwitch(self, status:bool): #Set the switch position
        if self.isSwitch == True:
            self.switchStatus = status
        else:
            print("Track is not a Switch")

    def getSwitch(self): #Get current switch position
        return self.switchStatus

    def setCrossroad(self, status:bool): #Set crossroad status
        if self.isCrossroad == True:
            self.crossroadStatus = status
        else:
            print("Track does not contain crossroad")
    
    def getCrossroad(self): #Get crossroas status
        return self.crossroadStatus
    
    def setLight(self, status:bool):
        if self.isLight == True:
            self.lightStatus = status
        else:
            print("Track does not contain light")
    
    def getLight(self):
        return self.lightStatus
        