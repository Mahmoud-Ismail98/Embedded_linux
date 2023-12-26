import RPi.GPIO as GPIO
import time 

button = 13
led =26

def Init_pin():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(led,GPIO.OUT)
    GPIO.output(led,GPIO.LOW)
    
Init_pin()
while True:
    switch_state = GPIO.input(button)
    if switch_state==1:
        GPIO.output(led,GPIO.HIGH)
    else :
        GPIO.output(led,GPIO.LOW)   
        
    print(switch_state)
    
    
