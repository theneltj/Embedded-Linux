## Python shit
import Adafruit_BBIO.GPIO as GPIO
import numpy as np
import time


#PIN SETUP
sone = "P9_11"
stwo = "P9_13"
sthree = "P9_17"
sfour = "P9_19"
GPIO.setup(sone, GPIO.IN)
GPIO.setup(stwo, GPIO.IN)
GPIO.setup(sthree, GPIO.IN)
GPIO.setup(sfour, GPIO.IN)


print("BeagleBone")


#GET DIMENSIONS FOR SKETCH
cols = int(input("How wide do you want your sketch?   "))
rows = int(input("How tall do you want your sketch?   "))

voidchar = "  "
arr = np.full((rows, cols), voidchar)

xloc = 0
yloc = rows - 1
arr[yloc][xloc] = " +" 


#DEFINES FOR MOVEMENTS AND REPRINTS
def reprint():
    print(chr(27)+"[2J")
    for j in range((len(arr[0])+2)*2 - 1):
        print("0", end='')
    print("0")
    for i in range(len(arr)):
        print("0 ", end='')
        for j in range(len(arr[i])):
            print(arr[i][j], end='')
        print(" 0")
    for j in range((len(arr[0])+2)*2):
        print("0", end='')
    print()

def eventone (channel):
    global xloc
    global yloc
    if xloc > 0:
        xloc -= 1
        addMark()
    
    
def eventtwo (channel):
    global xloc
    global yloc
    if xloc < cols - 1:
        xloc += 1
        addMark()
    
def eventthree (channel):
    global xloc
    global yloc
    if yloc < rows - 1:
        yloc += 1
        addMark()
    
def eventfour (channel):
    global xloc
    global yloc
    if yloc > 0:
        yloc -= 1
        addMark()
    
def addMark():
    arr[yloc][xloc] = " +"
    reprint()    



#INTERRUPT SETUP
GPIO.add_event_detect(sone, GPIO.RISING, callback=eventone, bouncetime = 500)    
GPIO.add_event_detect(stwo, GPIO.RISING, callback=eventtwo)
GPIO.add_event_detect(sthree, GPIO.RISING, callback=eventthree)
GPIO.add_event_detect(sfour, GPIO.RISING, callback=eventfour)

reprint()


while True:
    time.sleep(0.01)