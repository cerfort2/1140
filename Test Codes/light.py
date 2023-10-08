import serial
import time

serialComm = serial.Serial('COM3', 9600)
serialComm.timeout = 1


while True:
    click = serialComm.readline().decode('ascii')
    time.sleep(.5)
    if click == 'red':
        print("Red Light")
    elif click == 'yellowyellow':
        print("Yellow Light")
    elif click == 'greengreen':
        print("Green Light")
        break


serialComm.close()