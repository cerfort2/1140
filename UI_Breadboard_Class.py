import serial
import time

serialComm = serial.Serial('COM3', 9600)
serialComm.timeout = 1

class Operations():
    def __init__(self):
        pass

    def changeLight(color):
        serialComm.write(color.encode())
        time.sleep(.5)

    def changeCrossroad(toggle):
        serialComm.write(toggle.encode())
        time.sleep(.5)

    def changeSwitch(toggle):
        serialComm.write(toggle.encode())
        time.sleep(.5)