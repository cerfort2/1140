
from time import sleep
# import I2C_LCD_driver
from datetime import datetime
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtCore import QObject
from Hardware_Train_Controller.HWTrainControllerUI import Ui_Form
from PyQt6.QtWidgets import QApplication
import serial
# arduinoData = serial.Serial('/dev/cu.usbmodem1101',115200)
import sys


class HWTrainControllerGUI(Ui_Form):


    def __init__(self):

        super().__init__()
        # self.ui = Ui_HardwareTrainController()
        # self.ui.setupUi(self)
        

        # self.timer_parent = QObject()
        # self.timer = QTimer(self.timer_parent)
        # self.timer.timeout.connect(self.changeMode)
        # self.timer.start(50)
        # self.connect()
        
        # self.engine_prev = False
        # self.signal_prev = False
        # self.brake_prev = False

        # if(self.hwtrain.brakeFailure == True):
        #     engineStatus = "True/end"
        # engineStatus = str(self.hwtrain.brakeFailure) + "/end"
        # arduinoData.write(engineStatus.encode())

        #annoucements will update based on button not timer
        # self.ui.annoucements_button.clicked.connect(self.updateAnnoucement_manual)

        # self.ui.mode.currentTextChanged.connect(self.changeMode)
        # self.ui.integral_gain.valueChanged.connect(self.update_manual)
        # self.ui.proportional_gain.valueChanged.connect(self.update_manual)
        # self.ui.service_brake.clicked.connect(self.toggleService)
        

    def connect(self):
        self.mode.currentTextChanged.connect(self.changeMode)
        self.proportional_gain.setMaximum(999)
        self.integral_gain.setMaximum(999)
        self.proportional_gain.setValue(400)
        self.integral_gain.setValue(20)





    def changeMode(self):
        selected_text = self.mode.currentText()

        #check for failures
        # if(self.hwtrain.brakeFailure == True):
        #     #change led
        # else if(self.hwtrain.engineFailure == True):

        # else if(self.hwtrain.signalFailure == True):
        
        #check failures


        # if(self.hwtrain.brakeFailure != self.engine_prev and self.hwtrain.engineFailure == False):
        #     engineStatus = "False/end"
        #     arduinoData.write(engineStatus.encode())
        # elif(self.hwtrain.brakeFailure != self.engine_prev and self.hwtrain.engineFailure == True):
        #     engineStatus = "True/end"
        #     arduinoData.write(engineStatus.encode())
        
        
        # self.hwtrain.calcPower()
        # self.ui.power.display(self.hwtrain.power)
        # self.ui.current_speed.display(self.hwtrain.currentSpeed)
        # self.ui.speed_limit.display(self.hwtrain.speedLimit)
        # self.ui.authority.display(self.hwtrain.authority)


        if selected_text == "Automatic":
            self.manual_speed.setEnabled(0)
            self.annoucements_button.setEnabled(0)
            self.service_brake.setEnabled(0)
            self.right_door.setEnabled(0)
            self.left_door.setEnabled(0)
            self.exterior_lights.setEnabled(0)
            self.interior_lights.setEnabled(0)
            self.manual_temperature.setEnabled(0)
            #self.update_auto()
            #self.hwtrain.manualmode = False
        else:
            self.manual_speed.setEnabled(1)
            self.annoucements_button.setEnabled(1)
            self.service_brake.setEnabled(1)
            self.right_door.setEnabled(1)
            self.left_door.setEnabled(1)
            self.exterior_lights.setEnabled(1)
            self.interior_lights.setEnabled(1)
            self.manual_temperature.setEnabled(1)
            #self.update_manual()
            #self.hwtrain.manualmode = True

    # def update_auto(self):
        
    #     self.ui.commanded_speed.display(self.hwtrain.ctcSpeed)

    #     #self.ui.annoucements.displayText(self.hwtrain.annoucement) #change display onto LCD, is annoucements only regarding next stop?

    #     self.ui.temperature.display(self.hwtrain.temperature)

    #     #doors,lights,service/ebrake will be represented on the circuit board using leds and switches.
        





    #def updateAnnoucement_manual(self):
        
    # def toggleService(self):

    #     self.serviceClicked = self.serviceClicked + 1

    #     if(self.serviceClicked == 1):
    #         self.hwtrain.serviceBrakeFlag = True
    #     elif(self.serviceClicked >= 2):
    #         self.serviceClicked = 0
    #         self.hwtrain.serviceBrakeFlag = False



    # def changeKI(self):
    #     self.hwtrain.setKi(self.ui.integral_gain.value())
    #     self.hwtrain.setBrakeFailure(True)

    # def changeKP(self):
    #     self.hwtrain.setKp(self.ui.integral_gain.value())

    #def changeCommanded_speed(self):





    def init_ui(self):
        self = Ui_Form()           #setup ui
        self.ui.setupUi(self)
  


    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HWTrainControllerGUI()
    window.show()
    sys.exit(app.exec())



