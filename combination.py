import serial
import time

serialComm = serial.Serial('COM3', 9600)
serialComm.timeout = 1

while True:
    choice = input("What to control: ")
    if(choice == "done"):
        break
    serialComm.write(choice.encode())
    time.sleep(.5)
    if(choice == "lights"):
        while True:
            color = input("What color: ")
            serialComm.write(color.encode())
            time.sleep(.5)
            if(color == "exit"):
                break
    elif(choice == "screen"):
        while True:
            display = input("What display: ")
            serialComm.write(display.encode())
            time.sleep(.5)
            if(display == "exit"):
                break

serialComm.close()