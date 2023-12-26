import RPi.GPIO as GPIO
import threading 

led =26
state= 0
def Toggle():
    global state
    if state==0:
        GPIO.output(led,GPIO.LOW)
        state = 1
    else :
        GPIO.output(led,GPIO.HIGH)
        state = 0
        
    t = threading.Timer(2,Toggle)
    t.start() 
                            
def Init_pin():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led,GPIO.OUT)
    GPIO.output(led,GPIO.LOW)
    
Init_pin()
Toggle()
while True:
      pass    
    
