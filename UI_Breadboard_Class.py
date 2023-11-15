import serial
import time

serialComm = serial.Serial('COM3', 115200)
serialComm.timeout = 1

class Operations():
    def __init__(self):
        pass
    
    #True = Red, False = Green
    def changeLight(self, color:bool): #Function to change breadboard light color
        light = "G"
        serialComm.write(light.encode())
        time.sleep(1.1)
        value_byte = b'\x01' if color else b'\x00'
        serialComm.write(value_byte)

    def switch(self, fromText:str, toText:str, position:bool): #Switches screen based off position given
        if position == True:
            status = "R" #Right
        elif position == False:
            status = "L" #Left
        serialComm.write(status.encode())
        time.sleep(1.1)
        serialComm.write(fromText.encode())
        time.sleep(1.1)
        serialComm.write(toText.encode())

    def crossroad(self, current:bool): #Crossroad to On/Off based of status given
        if current == False:
            status = "F" #Off
        elif current == True:
            status = "O" #On
        serialComm.write(status.encode())
        time.sleep(.5)

    def plcCode(self, occupancies:[bool]):
        status = "C"
        convertStr = ''.join(map(lambda x: '1' if x else '0', occupancies))
        strs = str(convertStr)
        serialComm.write(status.encode())
        time.sleep(1.1)
        serialComm.write((strs + '\0').encode())
        time.sleep(.2)
        newStates = serialComm.readline().decode()
        print(newStates)
        # bool_array = [c == '1' for c in newStates]
        # return bool_array
        