from HWTrainControllerUI import Ui_HardwareTrainController
from trainmodel import train_model_software
from PyQt6 import QtCore, QtGui, QtWidgets, QMainWindow,QApplication
from time import sleep
import I2C_LCD_driver
from datetime import datetime
from PyQt6.QtCore import QTimer
from PyQt6.QtCore import QObject


import sys


class HWTrainControllerGUI(QMainWindow):


    def __init__(self,Automatic):
        self.hwtrain = train_model_software()
        super().__init__()
        

        self.timer_parent = QObject()

        self.timer = QTimer(self.timer_parent)
        self.timer.timeout.connect(self.update_all)
        self.timer.start(50)
        self.proportional_gain.valueChanged.connect(self.disp_info)
        self.integral_gain.valueChanged.connect(self.disp_info)
        self.manual_speed.valueChanged.connect(self.setCommanded)
        self.e_brake.pressed.connect(self.stop_train)
        self.exterior_light.stateChanged(self.exterior_light_disp)
        self.interir_light.stateChanged(self.interior_light_disp)
        self.right_door.stateChanged(self.right_door_disp)
        self.left_door.stateChanged(self.left_door_disp)
        self.temperature.pressed(self.)



    def init_ui(self):
        self.ui = Ui_HardwareTrainController()           #setup ui
        self.ui.setupUi(self)
        self.changeMode()
       
        

    def update_all(self):

        self.commanded_speed.display(self.hwtrain.getManual_commanded())
        self.current_speed.display(self.hwtrain.getCurrent_speed())
        self.hwtrain.computeAuthority()
        self.hwtrain.calcPower()
        self.disp_info()

    def disp_info(self):

        mylcd = I2C_LCD_driver.lcd()

        mylcd.lcd_display_string("Temp:" + str(self.hwtrain.getTemperature()),1,0)
        mylcd.lcd_display_string("Power Value:" + str(self.hwtrain.getPower()),2,0)
        mylcd.lcd_display_string("Current Speed:" + str(self.hwtrain.getCurrent_speed()),3,0)
        mylcd.lcd_display_string("Authority:" + str(self.hwtrain.getAuthority()),4,0)
        mylcd.lcd_display_string("IG:" + str(self.hwtrain.getKi()),1,15)
        mylcd.lcd_display_string("PG:" + str(self.hwtrain.getKp()),2,15)
    
        sleep(.5)


    def setCommanded(self):
        self.commanded_speed.display(self.manual_speed.value())
        self.hwtrain.setManualCommandedSpeed(self.manual_speed.value())
  
    
    def stop_train(self):
        self.hwtrain.setManual_commanded(0)
        self.commanded_speed.display(0)
        self.power.display(0)
        self.current_speed.display(self.hwtrain.getCurrent_speed())
        self.hwtrain.ebrakePressed()

    def sendTemperature(self):
        self.hwtrain.setTemperature(self.temperature.value())
    
    def sendAnnoucements(self):
        self.hwtrain.setAnnoucement(self.annoucements.displayText())



    def changeMode(self):
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

 
    def annoucements_disp(self):

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

    def exterior_light_disp(self):
         
        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string("Notification: ",1,0)
        mylcd.lcd_display_string("The light one status",2,0)
        mylcd.lcd_display_string("was changed.",3,0)
        sleep(1.5)
        mylcd.lcd_clear()
        self.check_value()

    def interior_light_disp(self):
         
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
        



        
  


    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HWTrainControllerGUI()
    window.show()
    sys.exit(app.exec())



