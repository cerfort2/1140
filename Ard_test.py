import serial
import time
from vpython import *

serialComm = serial.Serial('COM3', 9600)
serialComm.timeout = 1


while True:
    i = input("input: ").strip()
    if i == 'done':
        break
    serialComm.write(i.encode())
    time.sleep(.5)
    print(serialComm.readline().decode('ascii'))

serialComm.close()
