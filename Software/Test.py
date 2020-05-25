import time
import os
try: 
    from MotorControl import forward
except ImportError as x:
    print("cannot import "+str(x)+" function from its module (Error Code: 0004)")
try:
    from MotorControl import backwards
except ImportError as x:
    print("cannot import "+str(x)+" function from its module (Error Code: 0005)")

try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    print("installing the necessary modules please wait... (Error Code: 0003)")
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

if(__init__ == "__main__"):
    SystemTest()
