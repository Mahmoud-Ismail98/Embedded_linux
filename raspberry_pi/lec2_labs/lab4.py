import RPi.GPIO as GPIO
import time 

led =26

def Init_pin():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led,GPIO.OUT)
    GPIO.output(led,GPIO.LOW)
    
Init_pin()
while True:
    GPIO.output(led,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(led,GPIO.LOW)
    time.sleep(5)        
    
