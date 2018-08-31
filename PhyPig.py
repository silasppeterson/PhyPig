# main file for PhyPig

import RPi.GPIO as GPIO
import time

GPIO.setwarnings (False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(25, GPIO.IN)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
ledstate = 0

    
while True:
     #check button and change state
    if not GPIO.input(25):
        button=1
        while button:
            if GPIO.input(25):
                button=0
            time.sleep(.1)
        if ledstate==4:
            ledstate=0
        else:
            ledstate=ledstate+1
    
   
    # Set Leds based on state
    # state 0 all off
    if ledstate==0:
        GPIO.output (18, False)
        GPIO.output (27, False)
        GPIO.output (4, False)
        GPIO.output (26, False)

    # state 1 turns red on
    if ledstate==1:
        GPIO.output (18, True)
    # state 2 turns green on
    if ledstate==2:
        GPIO.output (4, True)
     # state 3 turns blue on
    if ledstate==3:
        GPIO.output (27, True)
    # state 4 turns yellow on
    if ledstate==4:
        GPIO.output (26, True)
      
        
    
            
