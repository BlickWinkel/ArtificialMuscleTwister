"""
Program Akışı;

Asansör Motor M1
Asansör Ucu Motor M2
Kanca Motor M3
Bobin Kayar Motor M4
Limit Switch Asansör LimSW1
Limit Switch Bobin LimSW2
Select Button Bttn1
Stop Button Bttn2

-Program başlayınca motorlar başlangıç konumuna gelmeli.
    -Asansör motor M1
    -bobin kayar mekanizma M4
    -2 adet limit switchten haber beklenecek
    -asansör mekanizması önce yukarı sonra aşağı inecek.
-"misinayı yerleştiriniz"
-"yerleştirdikten sonra 'y' yazıp enterlayınız.
-"misinanın boutunu giriniz"
-misina gerginleştirilir.
    -boyut bilgisine göre asansör mekanizma yukarı çıkacak. M1
-"lütfen misinanın üst ucuna bakır teli iliştiriniz."
-"işlem tamamlandıktan sonra 'y' yazıp enter tuşuna basınız."
-bakır tel sarım işlemi başlıyor
    -bobin kayar motor aşağı M4
    -asansör ucu ve kanca motor misinayı aynı yönde ( programda zıt!!)  M2 ve M3
-"sarım bitti. bakır teli kesiniz."
-"kestikten sonra 'y' yazıp enter tuşuna basınız."
-bobin kayar mekanizma başlangıç pozisyonuna
-"işlem başlıyor"
    -kanca motor ve asansör ucu motor M3 ve M2
    -asansör motoru M1 daha az bir adımla aşağı
    -M1 belirli bir adım yapınca programı durdur.
-sürekli olarak Stop buton kontrolü yap

"""
"""
pin bağlantıları;

Motor1  M1IN1 -->> GPIO4
        M1IN2 -->> GPIO17
        M1IN3 -->> GPIO27
        M1IN4 -->> GPIO22


Motor2  M2IN1 -->> GPIO5
        M2IN2 -->> GPIO6
        M2IN3 -->> GPIO16
        M2IN4 -->> GPIO12


Motor3  M3IN1 -->> GPIO25
        M3IN2 -->> GPIO24
        M3IN3 -->> GPIO23
        M3IN4 -->> GPIO13


Motor4  M4IN1 -->> GPIO2
        M4IN2 -->> GPIO3
        M4IN3 -->> GPIO7
        M4IN4 -->> GPIO8

LimSW1 -->> GPIO21

LimSW2 -->> GPIO20

Bttn1  -->> GPIO19

Bttn2  -->> GPIO26

"""
import time
import os
from MotorControl import forward
from MotorControl import backwards
from MotorControl import bimotor
from MotorControl import bimotor2
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    print("installing the necessary modules please wait...")
    moduleProceed = input("Do you want to proceed (y/n):")
    if(moduleProceed == "y"):
        os.system("python -m pip install RPi")
    else:
        exit()
#pins

#for the lift control motor as M1

M1in1 = 4
M1in2 = 17
M1in3 = 27
M1in4 = 22

#for the motor on the lift as M2

M2in1 = 5
M2in2 = 6
M2in3 = 16
M2in4 = 12

#for the twister motor as M3 

M3in1 = 25
M3in2 = 24
M3in3 = 23
M3in4 = 13

#for the resistance wire feeder motor as M4

M4in1 = 2
M4in2 = 3
M4in3 = 7
M4in4 = 8

#for lift control motor  M1 limit switch 
LimSW1 = 21
GPIO.setup(LimSW1, GPIO.IN)

#for resistance feeder motor M4 limit switch
LimSW2 = 20
GPIO.setup(LimSW2, GPIO.IN)

#for Select button 
Bttn1 = 19
GPIO.setup(Bttn1, GPIO.IN)

#for Emergency Stop button 
Bttn2 = 26
GPIO.setup(Bttn2, GPIO.IN)

while (GPIO.input(Bttn2)==0): #program will work until emergency button is pressed or user decide not to restart the program.
    print("Artificial Muscle Twister v1.0 \n Author: Emin Basoren \n Welcome to Aritificial Muscle Twister program. \n ! Please check the pins twice !")
    diagnosticProceed = input("Do you want to Test the motors and Buttons? (y/n):")
    if(diagnosticProceed == "y"):
        #test program
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
        if((GPIO.input(Bttn1)==1))
            print("Select Button works quite good")
        print("please press the emergency stop button..")
        if((GPIO.input(Bttn2)==1))
            print("Emergency Stop Button works quite good")
        
    else:
        proceedKey = input("please write 'y' and hit enter to proceed... if you dont want to proceed write 'n' instead of 'y' and hit enter... \n")
        if(str(proceedKey) == 'y'):
            print("Here it begins...")
            time.sleep(1)
            while(GPIO.input(LimSW1)==0): #Lift mechanism will rise until touches the limit switch
                forward(0.1,1,"M1") #M1
            while(GPIO.input(LimSW2)==0): #Resistance wire slider mechanism will rise until touches the limit switch
                backwards(0.1,1,"M4") #M4
            len1 = 718.05 #length between the upper side of the lift mechanism and limit switch
            Step1 = (len1/1.25)*400 #1.25 is the step length of the threaded rod and 400 is the step motor's step count to make a one tour
            backwards(0.1,Step1,"M1") #M1
            length = input("please enter the length (in mm) of the fishing line you are going to use...")
            print("please attach the fishing line to twister motor and lift motor on both ends...")
            proceedKey2 = input("when you're done please write 'y' and hit enter...")
            if(str(proceedKey2) == 'y'):
                len2 = length-47.1 #47.1 is the length of hook to hook
                Step2 = (len2/1.25)*400
                forward(0.1,Step2,"M1") # clockwise move of M1 makes lift mechanism go up
                len3 = (789.9 - len2)-106 # 789.9 mm is the max length of the main threaded rod 106 is the length between limit switch1 and wire feeder 
                Step3 = (len3/1.25)*400
                forward(0.1,Step3,"M4") # clockwise move of M4 makes resistance wire slider mechanism go down
                print("please attach the resistance wire on the upper end of the fishing line...")
                proceedKey3 = input("when you're done please write 'y' and hit enter...")
                if(str(proceedKey3) == 'y'):
                    print("resistance wiring process starting")
                    len4 = 720.29-len3 #720.29 is the max length of wire feeder mechanism can go
                    Step4 = (len4/1.25)*400
                    bimotor(0.2,Step4,"M2","M3")
                    forward(1.25,Step4,"M4")
                    print("Please cut the resistance wire and make sure it is tight on the fishing line's both ends.")
                    proceedKey4 = input("when you're done please write 'y' and hit enter...")
                    if(str(proceedKey4) == 'y'):
                        while(GPIO.input(LimSW2)==0):
                            backwards(0.1,1,"M4") #M4
                        print("twisting process starting")
                        bimotor2(0.2,Step2,"M2","M3")
                        backwards(0.4,Step2,"M1")
                        print("Process finished. Program will restart shortly after this.")
                        proceedKey5 = input("If you dont want the program to restart please write 'y' and hit enter...")
                        if(proceedKey5 == "y"):
                            break;
                    else:
                        print("Unable to detect what you want program will exit shortly...")
                        time.sleep(1)
                        exit()
                else:
                    print("Unable to detect what you want program will exit shortly...")
                    time.sleep(1)
                    exit()
            else:
                print("Unable to detect what you want program will exit shortly...")
                time.sleep(1)
                exit()
        if(proceedKey=="n"):
            exit()
        else:
            print("Unable to detect what you want program will exit shortly...")
            time.sleep(1)
            exit()