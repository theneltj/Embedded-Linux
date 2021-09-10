## Python shit
import Adafruit_BBIO.GPIO as GPIO
import numpy as np



def reprint():
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end='')
        print()



print("BeagleBone")

GPIO.setup("P8_14", GPIO.IN)


cols = int(input("How wide do you want your sketch?   "))
rows = int(input("How tall do you want your sketch?   "))

voidchar = '   '
arr = np.full((rows, cols), voidchar)

xloc = 0
yloc = rows - 1

if arr[xloc][yloc] == voidchar:
    position = [int(cols * yloc + xloc)]
    np.put(arr, position, ' + ')

reprint()

while True:
    direct = input("Enter direction (U/D/L/R):  ")
    #if GPIO.input("P8_14"):
    #    xloc += 1
    if direct == 'U' and yloc >= 0:
        yloc -= 1
    if direct == 'D' and yloc < rows:
        yloc += 1
    if direct == 'L' and xloc >= 0:
        xloc -= 1
    if direct == 'R' and xloc < cols:
        xloc += 1
    
    #print("X ", xloc)
    #print("Y ", yloc)
    
        
    if arr[xloc][yloc] == voidchar:
        position = [int(cols * yloc + xloc)]
        np.put(arr, position, ' + ')
    reprint()    
        
