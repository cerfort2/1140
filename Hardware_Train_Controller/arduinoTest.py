import serial
import time
arduinoData = serial.Serial('/dev/cu.usbmodem1101',115200)

manualmode = False
currentSpeed = 20
manualcommandedspeed = 30
ctcSpeed = 25
kp = 400
ki = 20

while True:
    values = f"{manualmode},{currentSpeed},{manualcommandedspeed},{ctcSpeed},{kp},{ki}\n"
    arduinoData.write(values.encode())


    arduino_data = arduinoData.readline().decode('utf-8', 'ignore').strip()
    power = arduino_data

    print(power)