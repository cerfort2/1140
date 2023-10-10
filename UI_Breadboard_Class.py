import serial
import time


serialComm = serial.Serial('COM3', 115200)
serialComm.timeout = 1

class Operations():
    def __init__(self):
        pass
    
    def changeLight(self, color): #Function to change breadboard light color
        light = "lights"
        serialComm.write(light.encode())
        time.sleep(1.1)
        check = str(color).lower()
        serialComm.write(check.encode())

    def switchLeft(self): #Switches switch left
        status = "switchLeft"
        serialComm.write(status.encode())
        time.sleep(.5)
    
    def switchRight(self): #Switches switch right
        status = "switchRight"
        serialComm.write(status.encode())
        time.sleep(.5)

    def crossroadOn(self):
        status = "crossroadOn"
        serialComm.write(status.encode())
        time.sleep(.5)

    def crossroadOff(self):
        status = "crossroadOff"
        serialComm.write(status.encode())
        time.sleep(.5)