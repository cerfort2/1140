from HWTrainControllerUI import Ui_HardwareTrainController
from HardwareTrainController import HardwareTrainController
from trainmodel import train_model_software
from time import sleep
import I2C_LCD_driver
from datetime import datetime
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QApplication
import serial


import sys


class HWTrainControllerGUI(QMainWindow):


    def __init__(self):
        super().__init__()
        self.hwtrain = HardwareTrainController()
        self.ui = Ui_HardwareTrainController()
        self.ui.setupUi(self)

        #arduino setup
        # EngineData = serial.Engine('com3',115200)
        # SignalData = serial.Signal('com3',115200)
        # BrakeData = serial.Brake('com3',115200)
        

        self.timer_parent = QObject()
        self.timer = QTimer(self.timer_parent)
        self.timer.timeout.connect(self.changeMode)
        self.timer.start(50)

        
        self.ui.mode.currentTextChanged.connect(self.changeMode)
        self.ui.integral_gain.valueChanged.connect(self.changeKI)
        self.ui.proportional_gain.valueChanged.connect(self.changeKP)
        self.ui.annoucements_button.clicked.connect(self.updateAnnoucement_manual)


     

    def changeMode(self):
        selected_text = self.ui.mode.currentText()

        #check for failures
        # if(self.hwtrain.brakeFailure == True):
        #     #change led
        # else if(self.hwtrain.engineFailure == True):

        # else if(self.hwtrain.signalFailure == True):
        

        
        self.hwtrain.calcPower()
        self.ui.power.display(self.hwtrain.power)
        
        self.ui.current_speed.display(self.hwtrain.currentSpeed)
        self.ui.speed_limit.display(self.hwtrain.speedLimit)
        self.ui.authority.display(self.hwtrain.authority)




        if selected_text == "Automatic":
            self.ui.manual_speed.setEnabled(0)
            self.ui.annoucements_button.setEnabled(0)
            self.ui.service_slider.setEnabled(0)
            self.ui.right_door.setEnabled(0)
            self.ui.left_door.setEnabled(0)
            self.ui.exterior_lights.setEnabled(0)
            self.ui.interior_lights.setEnabled(0)
            self.ui.manual_temperature.setEnabled(0)
            self.update_auto()
            self.hwtrain.manualmode = False
        else:
            self.ui.manual_speed.setEnabled(1)
            self.ui.annoucements_button.setEnabled(1)
            self.ui.service_slider.setEnabled(1)
            self.ui.right_door.setEnabled(1)
            self.ui.left_door.setEnabled(1)
            self.ui.exterior_lights.setEnabled(1)
            self.ui.interior_lights.setEnabled(1)
            self.ui.manual_temperature.setEnabled(1)
            #self.update_manual()
            self.hwtrain.manualmode = True

    def update_auto(self):
        
        self.ui.commanded_speed.display(self.hwtrain.ctcSpeed)

        self.ui.annoucements.displayText(self.hwtrain.annoucement) #change display onto LCD, is annoucements only regarding next stop?

        self.ui.temperature.display(self.hwtrain.temperature)

        #doors,lights,service/ebrake will be represented on the circuit board using leds and switches.
        
    def update_manual(self):

        self.ui.commanded_speed.display(self.ui.manual_speed.value())
        
        self.hwtrain.setCommanded_speed(self.ui.manual_speed.value())



    def updateAnnoucement_manual(self):
        




    def changeKI(self):
        self.hwtrain.setKi(self.ui.integral_gain.value())

    def changeKP(self):
        self.hwtrain.setKp(self.ui.integral_gain.value())




    def init_ui(self):
        self.ui = Ui_HardwareTrainController()           #setup ui
        self.ui.setupUi(self)
        self.changeMode()
  


    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HWTrainControllerGUI()
    window.show()
    sys.exit(app.exec())



