import serial
import time

serialComm = serial.Serial('COM3', 9600)
serialComm.timeout = 1

class Operations():
    def __init__(self):
        pass
    
    def changeLight(self, color): #Function to change breadboard light color
        light = "lights"
        serialComm.write(light.encode())
        time.sleep(1.2)
        check = str(color).lower()
        serialComm.write(check.encode())

    def changeCrossroad(self): #Function to change breadboard crossroad status
        status = "crossroad"
        serialComm.write(status.encode())

    def changeSwitch(self): #Function to change breadboard switch status
        status = "switch"
        serialComm.write(status.encode())