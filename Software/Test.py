import time
import os
from MotorControl import forward
from MotorControl import backwards
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    print("installing the necessary modules please wait...")
    moduleProceed = input("Do you want to proceed (y/n):")
    if(moduleProceed == "y"):
        os.system("python -m pip install RPi")
    else:
        exit()
#for Select button 
Bttn1 = 19
GPIO.setup(Bttn1, GPIO.IN)

#for Emergency Stop button 
Bttn2 = 26
GPIO.setup(Bttn2, GPIO.IN)

def SystemTest():
    print("test program starting")
    forward(1,1,"M1")
    time.sleep(1)
    backwards(1,1,"M1")
    time.sleep(1)
    forward(1,1,"M2")
    time.sleep(1)
    backwards(1,1,"M2")
    time.sleep(1)
    forward(1,1,"M3")
    time.sleep(1)
    backwards(1,1,"M3")
    time.sleep(1)
    forward(1,1,"M4")
    time.sleep(1)
    backwards(1,1,"M4")
    time.sleep(1)
    print("please press the select button..")
    if((GPIO.input(Bttn1)==1)):
        print("Select Button works quite good")
    print("please press the emergency stop button..")
    if((GPIO.input(Bttn2)==1)):
        print("Emergency Stop Button works quite good")
