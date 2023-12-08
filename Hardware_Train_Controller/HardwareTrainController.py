from PyQt6.QtWidgets import *
from HWTrainControllerGUI import *
import serial
import time
#arduinoData = serial.Serial('/dev/cu.usbmodem11101',115200)





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
        self.annoucement = ""
        self.authority = 100
        self.brakeFailure = False
        self.signalFailure = False
        self.engineFailure = False
        self.tunnel = False
        self.stationOnLeft = False
        self.stationOnRight = False
        self.rightdoor = False
        self.leftdoor = False
        self.manualcommandedspeed = 0
        self.temperature = 0
        self.power = 0
        self.ctcSpeed = 5
        self.currentSpeed = 0
        self.speedLimit = 43
        self.dwelling = False
        self.manualmode = False
        self.exterior = False
        self.interior = False
        self.brakeAuthority = 0
        self.brakeSpeed = 0
        self.serviceBrake= False
        self.eBrake = False
        self.dwellTime = 10
        self.e_k = 0
        self.e_k_prev = 0
        self.u_k = 0
        self.u_k_prev = 0
        self.kp = 400
        self.ki = 20
        self.service_button = False
        self.brakedistance = 0
        self.interval = 1


        self.ui = HWTrainControllerGUI()

    
    def configure_service(self):
        self.ui.service_brake.setCheckable(True)
        self.ui.service_brake.clicked.connect(self.getServiceBrake)
    
    def configure_ebrake(self):
        self.ui.ebrake.setCheckable(True)
        self.ui.ebrake.clicked.connect(self.getEbrake)

    def getServiceBrake(self):
        #self.service_clicked = self.service_clicked + 1
        self.serviceBrake = not self.serviceBrake

    def getEbrake(self):
        self.eBrake = not self.eBrake


    
    

    




    def train_communications(self):

        self.configure_service()
        self.configure_ebrake()
        #self.ui.service_brake.pressed.connect(self.manual_service)
        #retreive values
        self.ki=self.ui.integral_gain.value()
        self.kp=self.ui.proportional_gain.value()

        if(self.ui.mode.currentText() == "Manual"):
            self.setManualMode(True)
            self.ui.commanded_speed.display(self.manualcommandedspeed*2.2369362)
        else:
            self.setManualMode(False)
            self.ui.commanded_speed.display(self.ctcSpeed*2.2369362)


        self.manualcommandedspeed = self.ui.manual_speed.value()

        
        
        #Switching

        #calculate
        #use self.calcPower() if manual does not work.
        self.calcPower()
        #self.update_power()
        self.computeAuthority()
        self.computeDwellTime()
        self.computeServiceBrake()
        
        
        #if(not self.manualmode):
           # self.computeServiceBrake()
        
      
        #self.eBrakePressed()



        #update values
        self.ui.power.display(self.power)
        self.ui.current_speed.display(self.currentSpeed*2.2369362921)
        #self.ui.commanded_speed.display(self.manualcommandedspeed*2.2369362921)
        self.ui.speed_limit.display(self.speedLimit)
        self.ui.authority.display(self.authority)
        #arduino
        #self.engine_status()
        # self.signal_status()




    

    #emitting signals for both modes automatic/manual

    # def getServiceBrake(self):
    #     self.trainmodel_HW_servicebrake(self.serviceBrakeFlag)

    # def getPower(self):
    #     self.trainmodel_HW_power.emit(self.power)
    
    # def getEbrake(self):
    #     self.trainmodel_HW_ebrake.emit(self.eBrakeFlag)

    # #emitting manual signals

    # def getRD(self):
    #     self.trainmodel_HW_rightdoor.emit(self.rightdoor)
    
    # def getLD(self):
    #     self.trainmodel_HW_leftdoor.emit(self.leftdoor)

    # def getExterior(self):
    #     self.trainmodel_HW_exterior.emit(self.exterior)

    # def getInterior(self):
    #     self.trainmodel_HW_interior.emit(self.interior)
    
    # def getTemperature(self):
    #     self.trainmodel_HW_temperature(self.temperature)

    # def getAnnoucements(self):
    #     self.trainmodel_HW_temperature(self.annoucement)

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
        
        # pmax = 10

        # self.e_k_prev = self.e_k

        # self.u_k_prev = self.u_k

        # if(self.manualmode == False):
        #     self.e_k = self.ctcSpeed - self.currentSpeed
        # else:
        #     self.e_k = self.manualcommandedspeed - self.currentSpeed


        # self.u_k = self.u_k_prev + (.05)/2 * (self.e_k+self.e_k_prev)

        # val = self.kp*self.e_k + self.ki*self.u_k
        
        # altPower = self.kp * self.e_k + self.ki * self.u_k_prev

        # if(val >= pmax):
        #     self.power = altPower
        # else:
        #     self.power = val

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
            print(self.authority)
            print("power is set to 0")


        # arduinoData.write(values.encode())

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
            
            self.brakedistance = self.currentSpeed**2/(1.2)

            if self.brakedistance >= self.authority:
                
                self.serviceBrake=True 


            else:
                self.serviceBrake=False

            if self.dwelling:
                self.serviceBrake = False

            if self.serviceBrake==True:
                self.manualcommandedspeed=self.currentSpeed

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






    def getCommandedSpeed(self):
        return self.manualcommandedspeed
    
    def setManualMode(self,status):
        self.manualmode = status
    
    def computeAuthority(self):
        if self.authority<=0 and self.currentSpeed==0:
            if not self.manualmode:
                self.dwelling=True
    
    
    # def engine_status(self):
    #     if(self.engineFailure == True):
    #         arduinoData.write("True/end".encode())
    #     elif(self.engineFailure == False):
    #         arduinoData.write("False/end".encode())

    # def signal_status(self):
    #     if(self.signalFailure == True):
    #         signalStatus = "True/end"
    #         arduinoData.write(signalStatus.encode())
    #     elif(self.signalFailure == False):
    #         signalStatus = "False/end"
    #         arduinoData.write(signalStatus.encode())
    
    # def brake_status(self):

    # def update_power(self):
    #     values = f"{self.manualmode},{self.currentSpeed},{self.manualcommandedspeed},{self.ctcSpeed},{self.kp},{self.ki}\n"
    #     arduinoData.write(values.encode())

    #     arduino_data = arduinoData.readline().decode().strip()
    #     self.power = float(arduino_data)
    #     print(self.power)


    def open_GUI(self):
        self.widget1 = QWidget()
        self.ui.setupUi(self.widget1)
        self.ui.connect()
        self.widget1.show()


