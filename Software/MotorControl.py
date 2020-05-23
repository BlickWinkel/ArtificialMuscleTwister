import os
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    print("installing the necessary modules please wait...")
    moduleProceed = input("Do you want to proceed (y/n):")
    if(moduleProceed == "y"):
        os.system("python3 -m pip install RPi")
    else:
        exit()
import time
try:
    GPIO.setmode(GPIO.BCM) 
        
    #pins

    #for the lift control motor as M1

    M1in1 = 4
    M1in2 = 17
    M1in3 = 27
    M1in4 = 22
    GPIO.setup(M1in1, GPIO.OUT)
    GPIO.setup(M1in2, GPIO.OUT)
    GPIO.setup(M1in3, GPIO.OUT)
    GPIO.setup(M1in4, GPIO.OUT)

    #for the motor on the lift as M2

    M2in1 = 5
    M2in2 = 6
    M2in3 = 16
    M2in4 = 12
    GPIO.setup(M2in1, GPIO.OUT)
    GPIO.setup(M2in2, GPIO.OUT)
    GPIO.setup(M2in3, GPIO.OUT)
    GPIO.setup(M2in4, GPIO.OUT)

    #for the twister motor as M3 

    M3in1 = 25
    M3in2 = 24
    M3in3 = 23
    M3in4 = 13
    GPIO.setup(M3in1, GPIO.OUT)
    GPIO.setup(M3in2, GPIO.OUT)
    GPIO.setup(M3in3, GPIO.OUT)
    GPIO.setup(M3in4, GPIO.OUT)

    #for the resistance wire feeder motor as M4

    M4in1 = 2
    M4in2 = 3
    M4in3 = 7
    M4in4 = 8
    GPIO.setup(M4in1, GPIO.OUT)
    GPIO.setup(M4in2, GPIO.OUT)
    GPIO.setup(M4in3, GPIO.OUT)
    GPIO.setup(M4in4, GPIO.OUT)

    #for lift control motor  M1 limit switch 
    LimSW1 = 21
    GPIO.setup(LimSW1, GPIO.IN)

    #for resistance feeder motor M4 limit switch
    LimSW2 = 20
    GPIO.setup(LimSW2, GPIO.IN)

    def forward(delay, steps,MotorNO):
        for i in range(0, steps): 
            setStep(1, 0, 1, 0,MotorNO) 
            time.sleep(delay) 
            setStep(0, 1, 1, 0,MotorNO) 
            time.sleep(delay) 
            setStep(0, 1, 0, 1,MotorNO) 
            time.sleep(delay) 
            setStep(1, 0, 0, 1,MotorNO) 
            time.sleep(delay) 

    def bimotor(delay, steps,MotorNO1,MotorNo2):
        for i in range(0, steps): 
            setStep(1, 0, 1, 0,MotorNO1) 
            time.sleep(delay)
            setStep(1, 0, 0, 1,MotorNo2) 
            time.sleep(delay) 
            setStep(0, 1, 1, 0,MotorNO1) 
            time.sleep(delay)
            setStep(0, 1, 0, 1,MotorNo2) 
            time.sleep(delay)  
            setStep(0, 1, 0, 1,MotorNO1) 
            time.sleep(delay)
            setStep(0, 1, 1, 0,MotorNo2) 
            time.sleep(delay)  
            setStep(1, 0, 0, 1,MotorNO1) 
            time.sleep(delay)
            setStep(1, 0, 1, 0,MotorNo2) 
            time.sleep(delay) 
    def bimotor2(delay, steps,MotorNO1,MotorNO2):
        for i in range(0, steps):
            setStep(1, 0, 1, 0,MotorNO1) 
            time.sleep(delay)
            setStep(1, 0, 1, 0,MotorNO2) 
            time.sleep(delay) 
            setStep(0, 1, 1, 0,MotorNO1) 
            time.sleep(delay)
            setStep(0, 1, 1, 0,MotorNO2) 
            time.sleep(delay) 
            setStep(0, 1, 0, 1,MotorNO1) 
            time.sleep(delay)
            setStep(0, 1, 0, 1,MotorNO2) 
            time.sleep(delay) 
            setStep(1, 0, 0, 1,MotorNO1) 
            time.sleep(delay)
            setStep(1, 0, 0, 1,MotorNO2) 
            time.sleep(delay) 
    def backwards(delay, steps,MotorNO): 
        for i in range(0, steps): 
            setStep(1, 0, 0, 1,MotorNO) 
            time.sleep(delay) 
            setStep(0, 1, 0, 1,MotorNO) 
            time.sleep(delay) 
            setStep(0, 1, 1, 0,MotorNO) 
            time.sleep(delay) 
            setStep(1, 0, 1, 0,MotorNO) 
            time.sleep(delay) 

    def setStep(w1, w2, w3, w4, MotorNo): 
        if(MotorNO == "M1"):
            GPIO.output(M1in1, w1) 
            GPIO.output(M1in2, w2) 
            GPIO.output(M1in3, w3) 
            GPIO.output(M1in4, w4)
        if(MotorNO == "M2"):
            GPIO.output(M2in1, w1) 
            GPIO.output(M2in2, w2) 
            GPIO.output(M2in3, w3) 
            GPIO.output(M2in4, w4)

        if(MotorNO == "M3"):
            GPIO.output(M3in1, w1) 
            GPIO.output(M3in2, w2) 
            GPIO.output(M3in3, w3) 
            GPIO.output(M3in4, w4)

        if(MotorNO == "M4"):
            GPIO.output(M4in1, w1) 
            GPIO.output(M4in2, w2) 
            GPIO.output(M4in3, w3) 
            GPIO.output(M4in4, w4)
except NameError as exception:
    if(exception== "GPIO"): 
        print("RPi library causing the error. You should install on the terminal by writing this command 'python -m pip install RPi' ")
