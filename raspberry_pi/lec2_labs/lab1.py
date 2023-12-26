import os
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

while True:
    x =int(input("plz enter value "))
    if x == 0:
        GPIO.output(26, GPIO.LOW)   
    elif x == 1:
        GPIO.output(26, GPIO.HIGH)       
    else:
        print("print incorrect value")    
