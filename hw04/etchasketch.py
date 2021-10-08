## Python shit
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
from flask import Flask, render_template, request
import numpy as np
import smbus
import time
app = Flask(__name__)




bus = smbus.SMBus(2)  # Use i2c bus 2
matrix = 0x70         # Use address 0x70

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

#first byte green second red
leds = [0x00, 0x0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

sone = "P9_14"
GPIO.setup(sone, GPIO.IN)


print("BeagleBone")


#GET DIMENSIONS FOR SKETCH
#cols = int(input("How wide do you want your sketch?   "))
#rows = int(input("How tall do you want your sketch?   "))
cols = 8
rows = 8


voidchar = False
arr = np.full((rows, cols), voidchar)

xloc = 0
yloc = 0
arr[yloc][xloc] = True


#DEFINES FOR MOVEMENTS AND REPRINTS
def reprintled():
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] == True):
                leds[2*j + 1] = leds[2*j + 1] | (0b00000001 << i) #SHIFTS TO RIGHT COLUMN AND ADJUSTS BITS FOR COLOR
                bus.write_i2c_block_data(matrix, 0, leds)
                #print("Row: ", i, "Col: ", j, "VALUE OF COL: ", end='')
                #print(hex(leds[2*j + 1]))


def eventone (channel):
    global leds
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = False
            #print(arr[i][j], end='')
        #print()
    leds = [0x00, 0x0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    
    #time.sleep(1)
    addMark()
    #print("BUTTON")
    
def addMark():
    arr[yloc][xloc] = "True"
    reprintled()    
    

#Calls to movement using rotary    
def rotleft():
    global xloc
    global yloc
    if xloc > 0:
        xloc -= 1
        addMark()
    #print("LEFT")

def rotright():
    global xloc
    global yloc
    if xloc < cols - 1:
        xloc += 1
        addMark()
    #print("RIGHT")

def rotdown():
    global xloc
    global yloc
    if yloc > 0:
        yloc -= 1
        addMark()
    #print("DOWN")
    
def rotup():
    global xloc
    global yloc
    if yloc < rows - 1:
        yloc += 1
        addMark()
    #print("UP")
    



reprintled()

GPIO.add_event_detect(sone, GPIO.RISING, callback=eventone, bouncetime = 50)    
    
    
templateData = {}    

@app.route("/")
def index():
	# Read Sensors Status
	return render_template('index3.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'cmd':
	    time.sleep(0.1)
	if action == "right":
		rotright()
	if action == "left":
		rotleft()
	if action == "up":
		rotup()
	if action == "down":
		rotdown()
		     
	return render_template('index3.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8090, debug=True)
   
   
   
while True:
    time.sleep(0.1)
    