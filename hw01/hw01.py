#!/usr/bin/env python3
#Tyler Thenell
#Homework 1
#Etch a sketch game
import Adafruit_BBIO.GPIO as GPIO
import numpy as np
import time



print("BeagleBone")


#GET DIMENSIONS FOR SKETCH
cols = int(input("How wide do you want your sketch?   "))
rows = int(input("How tall do you want your sketch?   "))

# Set up array
voidchar = "  "
arr = np.full((rows, cols), voidchar)

#Place intial cursor location
xloc = 0
yloc = rows - 1
arr[yloc][xloc] = " +" 


#clears the screen and reprints the window with all cursors
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


reprint()


while True:
    #receive keybroard inputs
    direct = input("Enter direction (U/D/L/R):  ")
    
    #Adjust cursor position based on keyboard input
    if direct == 'U' and yloc > 0:
        yloc -= 1
    if direct == 'D' and yloc < rows - 1:
        yloc += 1
    if direct == 'L' and xloc > 0:
        xloc -= 1
    if direct == 'R' and xloc < cols - 1:
        xloc += 1
    
    #print("X ", xloc)
    #print("Y ", yloc)
    
    # If in a new position, change the value and reprint
    if arr[yloc][xloc] == voidchar:
        arr[yloc][xloc] = " +"
    reprint()    