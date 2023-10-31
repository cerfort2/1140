from HWTrainControllerUI import Ui_HardwareTrainController
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import RPi.GPIO as GPIO
import I2C_LCD_driver
from datetime import datetime
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QObject


import sys


class CustomAutomaticMode(Ui_HardwareTrainController):

    e_k = 0
    u_k = 0
    initial_authority = 0

    def __init__(self,Automatic):
        super().__init__()
        self.setupUi(Automatic)

        self.timer_parent = QObject()

        self.timer = QTimer(self.timer_parent)
        self.timer.timeout.connect(self.update_all)
        self.timer.start(50)
        self.setAuthority()
        self.mode.currentIndexChanged.connect(self.setAuto)
        self.proportional_gain.valueChanged.connect(self.check_value) #connects the widget to a function that continously checks if the value was updated
        self.integral_gain.valueChanged.connect(self.check_value)
        #self.service_slider.valueChanged.connect(self.update_sb)
        self.ebrake.clicked.connect(self.stop_train)
        self.speed_limit.display(43)
        self.annoucements_button.clicked.connect(self.annoucements_display) #connect to notify button

        self.right_door_status.stateChanged.connect(self.right_door_disp)
        self.left_door.stateChanged.connect(self.left_door_disp)
        self.exterior_lights.stateChanged.connect(self.light_one)
        self.interior_lights.stateChanged.connect(self.light_two)
        #self.ebrake_manual_2.stateChanged.connect(self.e_brake)
        #self.service_brake_tb.stateChanged.connect(self.service_brake) #change to slider
        #self.engine_failure.stateChanged.connect(self.engine_fail)
        #self.signal_failure.stateChanged.connect(self.signal_fail)
        #self.brake_failure.stateChanged.connect(self.brake_fail)




        #self.return_mylcd()

        self.check_value()

    def update_all(self):

        self.commanded_speed.display(self.manual_speed.value())
        self.current_speed.display(self.cs_test.value())
        #self.current_speed.display(value) get from train model
        self.calcAuthority()
        self.calcPower()
        self.check_value()

    def setAuto(self):
        selected_text = self.mode.currentText()

        if selected_text == "Automatic":
            self.manual_speed.setEnabled(0)
            self.annoucements_button.setEnabled(0)
            self.service_slider.setEnabled(0)
            self.right_door_status.setEnabled(0)
            self.left_door.setEnabled(0)
            self.exterior_lights.setEnabled(0)
            self.interior_lights.setEnabled(0)

        else:
            self.manual_speed.setEnabled(1)
            self.annoucements_button.setEnabled(1)
            self.service_slider.setEnabled(1)
            self.right_door_status.setEnabled(1)
            self.left_door.setEnabled(1)
            self.exterior_lights.setEnabled(1)
            self.interior_lights.setEnabled(1)

    
    def check_value(self):#displays info
        
        mylcd = I2C_LCD_driver.lcd()

        mylcd.lcd_display_string("Power Value:" + str(round(self.power.value())),2,0)
        mylcd.lcd_display_string("Velocity:" + str(round(self.commanded_speed.value())),3,0)
        mylcd.lcd_display_string("Authority:" + str(round(self.authority.value())),4,0)
        mylcd.lcd_display_string("IG:" + str(round(self.integral_gain.value())),1,15)
        mylcd.lcd_display_string("PG:" + str(round(self.proportional_gain.value())),2,15)
    
        sleep(.5)

    def stop_train(self):

        mylcd = I2C_LCD_driver.lcd()
        
        self.commanded_speed_auto.display(0)
        mylcd.lcd_display_string(str(0),3,10)
        
        self.check_value()
        

    def calcPower(self):
        
        pmax = 10
        kp = self.proportional_gain.value()
        ki = self.integral_gain.value()

        e_k_prev = CustomAutomaticMode.e_k

        u_k_prev = CustomAutomaticMode.u_k

        CustomAutomaticMode.e_k = self.commanded_speed.value() - self.current_speed.value() #current speed from train model

        CustomAutomaticMode.u_k = u_k_prev + (.05)/2 * (CustomAutomaticMode.e_k+e_k_prev)

        val = kp*CustomAutomaticMode.e_k + ki*CustomAutomaticMode.u_k
        
        altPower = kp * CustomAutomaticMode.e_k + ki * u_k_prev

        if(val >= pmax):
            self.power.display(altPower)
        else:
            self.power.display(val)

            
    
    def setAuthority(self):

        initial = CustomAutomaticMode.initial_authority
        self.authority.display(20)
        #this is just for testing, get it from train model

    def calcAuthority(self):
        newAuth = self.authority.value()-self.current_speed.value()

        if(newAuth <= 10):
            self.commanded_speed.display(self.commanded_speed.value()-1)
            self.authority.display(newAuth)

        if(newAuth <= 0):
            
            self.setAuthority()
            self.power.display(0)
        else:
            self.authority.display(newAuth)


    def getPower(self): #send power to train model

        return self.power_value_auto.value()
    
    def setCS(self):
        
        value = 0 #get current speed from train model
        self.current_speed.display(value)


    def annoucements_display(self):

        padding = " " * 12
      
        lcd = I2C_LCD_driver.lcd()
        my_long_string = self.annoucements_display_auto.displayText()
        #lcd.lcd_display_string("Annoucements: ",2,0)
        
        for i in range (0, len(my_long_string)):
            lcd.lcd_display_string("Annoucements: ",2,0)
            lcd_text = my_long_string[i:(i+20)]
            lcd.lcd_display_string(lcd_text,3)
            sleep(0.25)
            lcd.lcd_clear()
            #lcd.lcd_display_string(padding,3)
        
        lcd.lcd_clear()
        sleep(1)
        #lcd.lcd_clear()
        self.annoucements_display_auto.clear()
        self.check_value()



    def right_door_disp(self):
         
        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string("Notification: ",1,0)
        mylcd.lcd_display_string("The door status",2,0)
        mylcd.lcd_display_string("was changed.",3,0)
        sleep(1.5)
        mylcd.lcd_clear()
        self.check_value()
    
    def left_door_disp(self):
         
        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string("Notification: ",1,0)
        mylcd.lcd_display_string("The left status",2,0)
        mylcd.lcd_display_string("was changed.",3,0)
        sleep(1.5)
        mylcd.lcd_clear()
        self.check_value()

    def light_one(self):
         
        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string("Notification: ",1,0)
        mylcd.lcd_display_string("The light one status",2,0)
        mylcd.lcd_display_string("was changed.",3,0)
        sleep(1.5)
        mylcd.lcd_clear()
        self.check_value()

    def light_two(self):
         
        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string("Notification: ",1,0)
        mylcd.lcd_display_string("The light two status",2,0)
        mylcd.lcd_display_string("was changed.",3,0)
        sleep(1.5)
        mylcd.lcd_clear()
        self.check_value()

    def e_brake(self):
         
        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string("Notification: ",1,0)
        mylcd.lcd_display_string("The e-brake status",2,0)
        mylcd.lcd_display_string("was changed.",3,0)
        sleep(1.5)
        mylcd.lcd_clear()
        self.check_value()


    def tunnel_stat(self):
         
        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string("Notification: ",1,0)
        mylcd.lcd_display_string("The tunnel status",2,0)
        mylcd.lcd_display_string("was changed.",3,0)
        sleep(1.5)
        mylcd.lcd_clear()
        self.check_value()
        
    def moving_stat(self):
         
        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string("Notification: ",1,0)
        mylcd.lcd_display_string("The movement status",2,0)
        mylcd.lcd_display_string("was changed.",3,0)
        sleep(1.5)
        mylcd.lcd_clear()
        self.check_value()
    
    def stationary_stat(self):
         
        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string("Notification: ",1,0)
        mylcd.lcd_display_string("The stationary status",2,0)
        mylcd.lcd_display_string("was changed.",3,0)
        sleep(1.5)
        mylcd.lcd_clear()
        self.check_value()




app = QtWidgets.QApplication(sys.argv)
Automatic = QtWidgets.QMainWindow()
custom_ui = CustomAutomaticMode(Automatic)
Automatic.show()

sys.exit(app.exec_())