import tkinter as tk
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED=0
pin=0
def Toggle():
   global LED
   global pin
   #pin=pin_entery_num.get()
   LED ^=1
   if LED==1:   
         GPIO.output(pin, GPIO.HIGH)         
         print("LED ",pin,"is open")    
   elif LED==0:
        GPIO.output(pin, GPIO.LOW)   
        print("LED ",pin,"is closed") 

def init():
    global pin
    pin=int(pin_entery_num.get())
    GPIO.setup(pin,GPIO.OUT)
    print("configure LED",pin)
    
def Exit():
    main_window.destroy() 

main_window = tk.Tk()
main_window.title("LED Control")
main_window.geometry("400x200+150+150")
main_window.resizable(False,False)

toggle_button=tk.Button(main_window,text="toggle LED",command=Toggle)
configure_button=tk.Button(main_window,text="configure LED",command=init)
End_botton=tk.Button(main_window,text="Exit",command=Exit)
pin_entery_num=tk.Entry(main_window)

toggle_button.place(x=0,y=0)
configure_button.place(x=0,y=50)
End_botton.place(x=175,y=175)
pin_entery_num.place(x=200,y=0)
main_window.mainloop()
