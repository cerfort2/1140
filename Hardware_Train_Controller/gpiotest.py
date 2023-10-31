from time import sleep
import RPi.GPIO as GPIO
import I2C_LCD_driver
GPIO.setmode(GPIO.BOARD)#setting gpio output

#lcd configurations
mylcd = I2C_LCD_driver.lcd()
padding = " " * 10

L2_switch = 31 #GPIO pin 25
L1_switch = 29 #GPIO pin 24
RD_switch = 36 #GPIO Pin 16
LD_switch = 16 #GPIO pin 23

#configure switches
GPIO.setup(RD_switch,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(LD_switch,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(L1_switch,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(L2_switch,GPIO.IN,pull_up_down = GPIO.PUD_UP)
####################################################################
#gains
P_current_gain = 0
P_previous_gain  = 0 #get input from numpad

I_current_gain = 0
I_previous_gain = 0 #get from numpad
######################################################################
RD_current_state = 0
RD_previous_state = GPIO.input(RD_switch)

LD_current_state = 0
LD_previous_state = GPIO.input(LD_switch)

L2_current_state = 0
L2_previous_state = GPIO.input(L1_switch)

L1_current_state = 0
L1_previous_state = GPIO.input(L2_switch)


#print idle states
if GPIO.input(RD_switch) == 0:
    print("Right Door Opened")
       
else:
    print("Right Door Closed")
    
    
if GPIO.input(LD_switch) == 0:
    print("Left Door Opened")
      
else:
    print("Left Door Closed")
    
if GPIO.input(L1_switch) == 0:
    print("Light 1 turned on")
      
else:
    print("Light 1 turned off")
    

if GPIO.input(L2_switch) == 0:
    print("Light 2 turned on")
      
else:
    print("Light 2 turned off")
        

#############################################################
   
   #displaying scrolling text
    
    

def scrolling_text(padding = " " * 12, my_long_string = ""):
      
      for i in range (0, len(my_long_string)):
            lcd_text = my_long_string[i:(i+14)]
            mylcd.lcd_display_string(lcd_text,1)
            sleep(0.1)
            mylcd.lcd_display_string(padding,1)
                 
      sleep(0.25)
      mylcd.lcd_clear()

###############################################################
    
while True:
    #make all signals into functions
    #right door
    RD_current_state = GPIO.input(RD_switch)
    
    if(RD_current_state != RD_previous_state):
        if(RD_current_state == 0):
            scrolling_text(padding,"Notification: Samay is hardstuck gold for 5 years.")
            print("Right Door Opened.")
        else:
            print("Notification: Right Door has been closed")
    
    RD_previous_state = RD_current_state
##############################################################################   
    #left door
    LD_current_state = GPIO.input(LD_switch)
    
    if(LD_current_state != LD_previous_state):
            if(LD_current_state == 0):
                print("Left Door opened")#replace these print statements with whatever action needed.
            else:
                print("Left Door closed")
    
    LD_previous_state = LD_current_state
##########################################################################
    #light 1
    L1_current_state = GPIO.input(L1_switch)
    
    if(L1_current_state != L1_previous_state):
            if(L1_current_state == 0):
                print("Light 1 turned on")#replace these print statements with whatever action needed.
            else:
                print("Light 1 turned off")
    
    L1_previous_state = L1_current_state
###############################################################################
    #light 2
    L2_current_state = GPIO.input(L2_switch)
    
    if(L2_current_state != L2_previous_state):
            if(L2_current_state == 0):
                print("Light 2 turned on")#replace these print statements with whatever action needed.
            else:
                print("Light 2 turned off")
    
    L2_previous_state = L2_current_state
    
    
    sleep(.1)
    
    
##############################################################################################   
    
    #constant display power, mass, and velocity
    mylcd.lcd_display_string("Power Value: ",2,0)
    mylcd.lcd_display_string("Velocity: ",3,0)
    mylcd.lcd_display_string("Mass: ",4,0)
    mylcd.lcd_display_string("IG: " + str(I_current_gain),1,15)
    mylcd.lcd_display_string("PG: " + str(I_current_gain),2,15)
   # I_current_state = 1 #input value from numpad
    
   # if(I_current_state != I_previous_state)
       # mylcd.lcd_display_string("IG: " + str(I_current_state),1,15)
        
    
    
    
    
    
    
    
    
    
    
    
    
