from PyQt6.QtWidgets import *
from Hardware_Train_Controller.HWTrainControllerGUI import *
import serial
import time
#arduinoData = serial.Serial('COM3',115200, timeout = 1)
time.sleep(1)

class HardwareTrainController():
    
    # #both
    # trainmodel_HW_power = pyqtSignal(float)
    # trainmodel_HW_servicebrake = pyqtSignal(bool)
    # trainmodel_HW_ebrake = pyqtSignal(bool)
    

    # #manual
    # trainmodel_HW_rightdoor = pyqtSignal(bool)
    # trainmodel_HW_leftdoor = pyqtSignal(bool)
    # trainmodel_HW_exterior = pyqtSignal(bool)
    # trainmodel_HW_interior = pyqtSignal(bool)
    # trainmodel_HW_temperature = pyqtSignal(bool)
    # trainmodel_HW_annoucements = pyqtSignal(bool)


    
    def __init__(self):
        self.service_clicked = 0
        self.beaconInfo = []
        self.nextstop = ""
        self.announcement = ""
        self.authority = 100
        self.brakeFailure = False
        self.signalFailure = False
        self.engineFailure = False
        self.tunnel = False
        self.stationOnLeft = False
        self.stationOnRight = False
        self.rightdoor = False
        self.leftdoor = False
        self.manualcommandedspeed = 5
        self.temperature = 0
        self.power = 0
        self.ctcSpeed = 5
        self.currentSpeed = 3
        self.speedLimit = 43
        self.dwelling = False
        self.manualmode = False
        self.exterior = True
        self.interior = False
        self.brakeAuthority = 0
        self.brakeSpeed = 0
        self.serviceBrake= False
        self.eBrake = False
        self.dwellTime = 60
        self.e_k = 0
        self.e_k_prev = 0
        self.u_k = 0
        self.u_k_prev = 0
        self.kp = 400
        self.ki = 20
        self.brakedistance = 0
        self.interval = 1
        self.waysideStop = False
        self.stationOnLeft = 'l'
        self.stationOnRight = 'l'
        
        self.ui = HWTrainControllerGUI()

    def setCommandedSpeed(self,s):
        self.ctcSpeed=min(s, self.speedLimit)

    def getAnnouncement(self):
        return self.announcement
    def getLeftDoor(self):
    #open door based on where the station is and if you are dwelling
        if self.dwelling and self.stationOnLeft=='l':
            self.leftdoor=True
            self.rightdoor=False
            return True
        if self.dwelling and self.stationOnLeft=='r':
            self.rightdoor=True
            self.leftdoor=False
            return False
        else:
            return self.leftdoor
            
    def getRightDoor(self):
    #open door based on where the station is and if you are dwelling
        if self.dwelling and self.stationOnLeft=='l':
            self.leftdoor=True
            self.rightdoor=False
            return False
        if self.dwelling and self.stationOnLeft=='r':
            self.rightdoor=True
            self.leftdoor=False
            return True
        if self.dwelling and self.stationOnLeft=='b':
            self.rightdoor=True
            self.leftdoor=True
            return True
        else:
            return self.rightdoor
        
    def getExteriorLights(self):
        return self.exterior
    def getIntLights(self):
        return self.interior

    def setTrainNumber(self,n):
        self.trainnumber=n
    
    def activateWaysideStop(self):
        self.waysideStop=True    

    def deactivateWaysideStop(self):
        self.waysideStop=False 
        self.eBrake = False

    def setTemperature(self,x):
        self.temperature = x

    def configure_UI(self):
        self.ui.right_door.stateChanged.connect(self.getRD)
        self.ui.left_door.stateChanged.connect(self.getLD)
        self.ui.exterior_lights.stateChanged.connect(self.getExternal)
        self.ui.interior_lights.stateChanged.connect(self.getInterior)
        self.ui.service_brake.setCheckable(True)
        self.ui.service_brake.clicked.connect(self.getServiceBrake)
        self.ui.ebrake.setCheckable(True)
        self.ui.ebrake.clicked.connect(self.getEbrake)

    
    def getServiceBrake(self):
        #self.service_clicked = self.service_clicked + 1
        self.serviceBrake = not self.serviceBrake

    def getEbrake(self):
        self.eBrake = not self.eBrake

    def getRD(self,status):
        if status == 2:
            self.rightdoor = True
        else:
            self.rightdoor = False
    
    def getLD(self,status):
        if status == 2:
            self.leftdoor = True
        else:
            self.leftdoor = False

    
    def getExternal(self,status):
        if status == 2:
            self.exterior = True
        else:
            self.exterior = False
        
    def getInterior(self,status):
        if status == 2:
            self.interior = True
        else:
            self.interior = False


    def update_time(self):

        self.configure_UI()

        self.ki=self.ui.integral_gain.value()
        self.kp=self.ui.proportional_gain.value()  
        self.temperature = self.ui.manual_temperature.value()
        self.manualcommandedspeed = self.ui.manual_speed.value()

        if(self.engineFailure or self.signalFailure or self.brakeFailure):
            self.eBrake = True
        #calculate power, update_power() uses arduino logic to calculate power, calcPower() uses software. When implementing update_vals() the is problems seeing trains on the line, but engine failure function is present via leds
        self.calcPower()
        #self.update_vals()
        #self.update_power()
        self.computeAuthority()
        self.computeDwellTime()
        self.computeServiceBrake()

        if(self.currentSpeed < 1):
            self.currentSpeed = 0
        print(self.eBrake)


        #update values on UI
        self.ui.power.display(self.power)
        self.ui.current_speed.display(self.currentSpeed*2.2369362921)
        self.ui.speed_limit.display(self.speedLimit)
        self.ui.authority.display(self.authority)
        self.ui.temperature.display(self.temperature)

        if(self.ui.mode.currentText() == "Manual"):
            self.setManualMode(True)
            self.ui.commanded_speed.display(self.manualcommandedspeed*2.2369362)
        else:
            self.setManualMode(False)
            self.ui.commanded_speed.display(self.ctcSpeed*2.2369362)



    def getPower(self):
        return self.power
    
    def getManualMode(self):
        return self.manualmode
     
    
    def eBrakePressed(self): 
        if self.currentSpeed==0 and self.eBrake==True:    #ebrake already pressed
            print('Ebrake released')
            self.eBrake=False
        else:
            print('Ebrake pressed')
            self.eBrake=True

    def computeExtLights(self):
        if self.tunnel and not self.manualmode:
            self.exlights=True
        if not self.tunnel and not self.manualmode:
            self.exlights=False
        return self.exlights

    def setCTC(self,x):
        self.ctcSpeed = x
        
    def setBeaconInfo(self,s):
        self.beaconInfo=s

    def setCurrentSpeed(self,s):
        self.currentSpeed=s

    def setSpeedLimit(self,s):
        self.speedLimit=s*2.2369362921
        if self.speedLimit>43:
            self.speedLimit=43
        
    def setNextStop(self,stop):
        self.nextstop=stop
        
    def setAnnouncement(self,a):
        self.announcement=a

    def setAuthority(self,a):
        self.authority=a
  
    def setBrakeFailure(self,a):
        self.brakeFailure=a

    def setSignalFailure(self,a):
        self.signalFailure=a

    def setEngineFailure(self,a):
        self.engineFailure=a

    def setTunnel(self,t):
        self.tunnel=t

    def setStationOnLeft(self, s):
        self.stationOnLeft=s

    def setStationOnRight(self,s):
        self.stationOnRight = s

    def setServiceBrakeSlide(self,s):
        self.serviceBrakeSlide=s

    def setTemperature(self,t):
        self.temperature=t

    def setCommanded_speed(self,x):
        self.manualcommandedspeed = x
    

    def calcPower(self):

        if self.manualmode==True:
            self.ek_prev=self.e_k
            self.e_k=(self.manualcommandedspeed-self.currentSpeed)
            self.u_k=(.05/2)*(self.e_k+self.ek_prev)
            self.power=(self.e_k*self.kp-self.ki*self.u_k)
        else:
            self.ek_prev=self.e_k
            self.e_k=(self.ctcSpeed-self.currentSpeed)
            self.u_k=(.05/2)*(self.e_k+self.ek_prev)
            self.power=(self.e_k*self.kp-self.ki*self.u_k)
            print("power is calculated")
            print(self.power)

        if self.power>120000:
            self.power=120000

        if self.brakeFailure or self.signalFailure or self.engineFailure or self.eBrake or self.power < 0 or self.serviceBrake or self.authority <= 0: #must change, this does not support failures
            self.power=0
            self.eBrake=0







    def setKi(self, k):
        self.ki=k

    def setKp(self, k):
        self.kp=k

    def getManual_commanded(self):
        return self.manualcommandedspeed
    
    def getCurrent_speed(self):
        return self.currentSpeed
    
    def getSpeedLimit(self):
        return self.speedLimit
    
    def getCTCspeed(self):
        return self.ctcSpeed
    
    def getAuthority(self):
        return self.authority
    
    def computeServiceBrake(self):
        
        if not self.manualmode:
            #determine the min distance to brake comfortably and get to the station
            self.brakedistance = self.currentSpeed**2/(1.2)

            if self.brakedistance>=self.authority or self.currentSpeed > self.ctcSpeed:
                self.serviceBrake=True
            else:
                self.serviceBrake=False

            #servicebrake is off if dwelling
            if self.dwelling:
                self.serviceBrake = False
            #service brake is on if wayside sends a red signal
            if self.waysideStop:
                self.eBrake=True
            elif not self.engineFailure and not self.brakeFailure and not self.signalFailure:
                self.eBrake = False

    def computeDwellTime(self):
        if self.dwelling and not self.manualmode:
            if (self.dwellTime-self.interval)>=0:   #subtract the time that it takes the timer to time out
                self.dwellTime-=self.interval
                print(self.dwellTime)
            else:
                self.dwelling=False
                self.serviceBrake = False
                self.eBrake = False
                self.brakedistance = 0
                self.authority = 100

            if self.waysideStop:
                self.eBrake = True
            else:
                self.eBrake = False






    def getCommandedSpeed(self):
        return self.manualcommandedspeed
    
    def setManualMode(self,status):
        self.manualmode = status
    
    def computeAuthority(self):
        if self.authority<=0 and self.currentSpeed==0:
            if not self.manualmode:
                self.dwelling=True
    
    def update_vals(self):
        self.mode_as_int = 0
        
        if self.manualmode:
            self.mode_as_int = 1
        else:
            self.mode_as_int = 0

        self.serviceb = int(self.serviceBrake)
        self.emergencybrake = int(self.eBrake)
        self.RD = int(self.rightdoor)
        self.LD = int(self.leftdoor)
        self.e_light = int(self.exterior)
        self.i_light = int(self.interior)
        self.e_failure = int(self.engineFailure)
        self.s_failure = int(self.signalFailure)
        self.b_failure = int(self.brakeFailure)

        values = f"{self.mode_as_int},{self.currentSpeed},{self.manualcommandedspeed},{self.ctcSpeed},{self.serviceb},{self.emergencybrake},{self.authority},{self.RD},{self.LD},{self.e_light},{self.i_light},{self.e_failure},{self.s_failure},{self.b_failure},{self.temperature}\n"
        arduinoData.write(values.encode())
        time.sleep(1)

    def update_power(self):
        #try to close and open arduino in this function to allow speed ups
        self.mode_as_int = 0
        
        if self.manualmode:
            self.mode_as_int = 1
        else:
            self.mode_as_int = 0

        self.serviceb = int(self.serviceBrake)
        self.emergencybrake = int(self.eBrake)
        self.RD = int(self.rightdoor)
        self.LD = int(self.leftdoor)
        self.e_light = int(self.exterior)
        self.i_light = int(self.interior)
        self.e_failure = int(self.engineFailure)
        self.s_failure = int(self.signalFailure)
        self.b_failure = int(self.brakeFailure)

        values = f"{self.mode_as_int},{self.currentSpeed},{self.manualcommandedspeed},{self.ctcSpeed},{self.serviceb},{self.emergencybrake},{self.authority},{self.RD},{self.LD},{self.e_light},{self.i_light},{self.e_failure},{self.s_failure},{self.b_failure},{self.temperature}\n"
        arduinoData.write(values.encode())
        time.sleep(1)

        arduino_data = arduinoData.readline().decode().strip()
        self.power = float(arduino_data)


    def open_GUI(self):
        self.widget1 = QWidget()
        self.ui.setupUi(self.widget1)
        self.ui.connect()
        self.widget1.show()


