import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets

from swtc import Ui_MainWindow



class SoftwareTrainControllerGUI(QMainWindow):

    #variables
    nextstop="a stop"
    currentSpeed=0      #current speed in manual or auto (max speed is 70km/hr)
    previousSpeed=0
    commandedSpeed=0    #commanded speed in automatic mode
    acceleration=0      # m/s^2
    authority=0         #authority in automatic mode
    mass=40.9              #in tons (max is 56.7)
    temperature=70       #temp in degrees fahrenheit
    exlights=False     #true=on
    intlights=False      #true=on
    leftDoor=False       #true=open
    rightDoor=False      #true=open
    announcement="hello"
    manualMode=False    #true =manual mode on
    eBrake=False        #false=not pressed
    serviceBrake=False  #false=not pressed
    kp=0    #proportional gain
    ki=0    #integral gain
    brakeFailure=False  # false is no failure
    engineFailure=False
    signalFailure=False
    time=1300
    force=0         # f=ma
    power=0     # p=fv  
    
        
    
    def __init__(self):
        super().__init__()
        self.init_ui()

        #cannot change the train failures in manual or automatic mode
        self.ui.manualbrakefailure_2.setDisabled(True)
        self.ui.manualenginefailure.setDisabled(True)
        self.ui.manualsignalfailure.setDisabled(True)
        self.ui.autobrakefailure.setDisabled(True)
        self.ui.autoenginefailure.setDisabled(True)
        self.ui.autosignalfailure.setDisabled(True)

        #cannot edit doors or light statuses in automatic mode
        self.ui.autoleftdoor.setDisabled(True)
        self.ui.autorightdoor.setDisabled(True)
        self.ui.autoexternallights.setDisabled(True)
        self.ui.autointernallights.setDisabled(True)
                
        

        self.ui.tbapply.clicked.connect(self.tbreceiveVals)         #check for if the apply button is pressed in the test bench
        self.ui.manualapply.clicked.connect(self.manualreceiveVals)   # check for if the apply button is pressed in the manual mode ui

        self.ui.autoebrake.clicked.connect(self.eBrakePressed)      #check for if ebrake is pushed in manual or automatic
        self.ui.manualebrake.clicked.connect(self.eBrakePressed)   

        self.ui.servicebrake.clicked.connect(self.serviceBrakePressed) #check for if service brake is pushed in manual mode

#still need to implement functionality for manual changes

    def serviceBrakePressed(self):
        if self.currentSpeed==0:
            print('Service Brake Pressed: Speed is already 0!')
            self.tbcomputeVals()
        else:
            print('Service Brake pressed')
            self.currentSpeed-=1
            self.acceleration=-1
            self.tbcomputeVals()

    def eBrakePressed(self):  
        if self.currentSpeed==0:
            print('Ebrake pressed: Speed is already 0!') 
        else:
            print('Ebrake pressed')
            self.currentSpeed=0
            self.acceleration=0
            self.tbcomputeVals()


    def manualreceiveVals(self):
        self.previousSpeed=self.currentSpeed
        self.currentSpeed=self.ui.manualspeed.value()
        self.temperature=self.ui.manualtemp.value()
        self.announcement=self.ui.manualannouncement.currentText()
        self.ki=self.ui.manualki.value()
        self.kp=self.ui.manualkp.value()
        self.exlights=self.ui.manualexternallight.checkState()
        self.intlights=self.ui.manualinternallight.checkState()
        self.leftDoor=self.ui.manualleftdoor.checkState()
        self.rightDoor=self.ui.manualrightdoor.checkState()
        self.manualcomputeVals()
    
    def manualcomputeVals(self):
        self.power=self.ki*self.currentSpeed+self.kp*self.previousSpeed
        self.manualudpateVals()

    def manualudpateVals(self):
        self.ui.manualpower.setText(str(self.power))
        self.ui.autopower.setText(str(self.power))
        self.ui.autocurrentspeed.setText(str(self.currentSpeed))
        self.ui.autoannouncement.setText(self.announcement)
        self.ui.autotemp.setText(str(self.temperature))
        self.ui.autoki.setText(str(self.ki))
        self.ui.autokp.setText(str(self.kp))
        self.ui.autoexternallights.setCheckState(self.ui.manualexternallight.checkState())
        self.ui.autointernallights.setCheckState(self.ui.manualinternallight.checkState())
        self.ui.autoleftdoor.setCheckState(self.ui.manualleftdoor.checkState())
        self.ui.autorightdoor.setCheckState(self.ui.manualrightdoor.checkState())



    def tbreceiveVals(self):                                              #receive values from test bench after apply button is pressed
        self.acceleration=int(self.ui.tbacceleration.toPlainText())
        self.previousSpeed=self.currentSpeed
        self.currentSpeed=int(self.ui.tbcurrentspeed.toPlainText())
        self.commandedSpeed=int(self.ui.tbcommandespeed.toPlainText())
        self.acceleration=int(self.ui.tbacceleration.toPlainText())
        self.authority=int(self.ui.tbauthority.toPlainText())
        self.mass=int(self.ui.tbmass.toPlainText())
        self.temperature=int(self.ui.tbtemp.toPlainText())
        self.kp=int(self.ui.tbkp.toPlainText())
        self.ki=int(self.ui.tbki.toPlainText())
        self.announcement=self.ui.tbannouncement.currentText()
        self.leftDoor=self.ui.tbleftdoor.checkState()
        self.rightDoor=self.ui.tbrightdoor.checkState()
        self.exlights=self.ui.tbexteriorlights.checkState()
        self.intlights=self.ui.tbinteriorlights.checkState()
        self.manualMode=self.ui.tbmanualmode.checkState()
        self.brakeFailure=self.ui.tbbrakefailure.checkState()
        self.engineFailure=self.ui.tbenginefailure.checkState()
        self.tbcomputeVals()
    
    def tbcomputeVals(self):
        self.power=self.ki*self.currentSpeed+self.kp*self.previousSpeed
        self.tbupdateVals()

    def tbupdateVals(self):
        #update manual mode values from tb
        self.ui.manualspeed.setValue(self.currentSpeed)
        self.ui.manualacceleration.setText(str(self.acceleration))
        self.ui.manualnextstop.setText("Station Square")
        self.ui.manualtime.setText(str(self.time))
        self.ui.manualmass.setText(str(self.mass))
        self.ui.manualtemp.setValue(self.temperature)
        self.ui.manualleftdoor.setCheckState(self.ui.tbleftdoor.checkState())
        self.ui.manualrightdoor.setCheckState(self.ui.tbrightdoor.checkState())
        self.ui.manualexternallight.setCheckState(self.ui.tbexteriorlights.checkState())
        self.ui.manualinternallight.setCheckState(self.ui.tbinteriorlights.checkState())
        self.ui.manualbrakefailure_2.setCheckState(self.ui.tbbrakefailure.checkState())
        self.ui.manualenginefailure.setCheckState(self.ui.tbenginefailure.checkState())
        self.ui.manualsignalfailure.setCheckState(self.ui.tbsignalfailure.checkState())
        self.ui.manualki.setValue(self.ki)
        self.ui.manualkp.setValue(self.kp)
        self.ui.manualannouncement.addItem(str(self.ui.tbannouncement.currentText()))
        self.ui.manualpower.setText(str(self.power))

        #update automatic mode values from tb
        self.ui.autocurrentspeed.setText(str(self.currentSpeed))
        self.ui.autocommandedspeed.setText(str(self.commandedSpeed))
        self.ui.autoacceleration.setText(str(self.acceleration))
        self.ui.autoauthority.setText(str(self.authority))
        self.ui.autonextstop.setText("Station Square")
        self.ui.autotime.setText(str(self.time))
        self.ui.automass.setText(str(self.mass))
        self.ui.autotemp.setText(str(self.temperature))
        self.ui.autoleftdoor.setCheckState(self.ui.tbleftdoor.checkState())
        self.ui.autorightdoor.setCheckState(self.ui.tbrightdoor.checkState())
        self.ui.autoexternallights.setCheckState(self.ui.tbexteriorlights.checkState())
        self.ui.autointernallights.setCheckState(self.ui.tbinteriorlights.checkState())
        self.ui.autobrakefailure.setCheckState(self.ui.tbbrakefailure.checkState())
        self.ui.autoenginefailure.setCheckState(self.ui.tbenginefailure.checkState())
        self.ui.autosignalfailure.setCheckState(self.ui.tbsignalfailure.checkState())
        self.ui.autoki.setText(str(self.ki))
        self.ui.autokp.setText(str(self.kp))
        self.ui.autoannouncement.setText(str(self.ui.tbannouncement.currentText()))
        self.ui.autopower.setText(str(self.power))

        
        

    def init_ui(self):
        self.ui = Ui_MainWindow()           #setup ui
        self.ui.setupUi(self)
        self.tbupdateVals() #set default vals
        
       # self.ui.tbcurrentspeed.textChanged.connect(lambda: self.updateVals)


        self.ui.tbannouncement.addItem('hello')
        self.ui.tbannouncement.addItem('Goodbye')
   

        #  # Create QTimer for service brake
        # self.service_brake_timer = QTimer(self)
        # self.service_brake_timer.timeout.connect(self.service_brake)
        # self.service_brake_timer.setInterval(1000)  # Decrease speed every second

    # def emergency_brake(self):
    #     # Add logic for emergency brake (set speed to 0)
    #     self.current_speed = 0
    #     self.update_speed_label()

    # def start_service_brake(self):
    #     #Start the service brake timer when the button is clicked
    #      self.service_brake_timer.start()

    # def service_brake(self):
    #     # Add logic for service brake (decrease speed by 3 per second until 0)
    #     if self.current_speed > 0:
    #         self.current_speed = max(0, self.current_speed - 3)
    #         self.update_speed_label()
    #     else:
    #         # Stop the timer when speed reaches 0
    #         self.service_brake_timer.stop()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SoftwareTrainControllerGUI()
    window.show()
    sys.exit(app.exec())
