import serial
import sys
import time

serialComm = serial.Serial('COM3', 9600)
serialComm.timeout = 1

while True:
    i = input("print: ")
    if i == 'done':
        break
    serialComm.write(i.encode())
    time.sleep(.5)


serialComm.close()