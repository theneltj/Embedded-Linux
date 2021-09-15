#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
import time

red = "P9_25"
blue = "P9_27"
yellow = "P9_29"
green = "P9_31"

sone = "P9_11"
stwo = "P9_13"
sthree = "P9_17"
sfour = "P9_19"




GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

GPIO.setup(sone, GPIO.IN)
GPIO.setup(stwo, GPIO.IN)
GPIO.setup(sthree, GPIO.IN)
GPIO.setup(sfour, GPIO.IN)

#while (True):
    #GPIO.output(blue, GPIO.HIGH)
    #GPIO.output(red, GPIO.HIGH)
    #GPIO.output(green, GPIO.HIGH)
    #GPIO.output(yellow, GPIO.HIGH)
    #time.sleep(0.2)
    #GPIO.output(blue, GPIO.LOW)
    #GPIO.output(red, GPIO.LOW)
    #GPIO.output(green, GPIO.LOW)
    #GPIO.output(yellow, GPIO.LOW)
    #time.sleep(0.2)

#events to toggle LED state
def eventone (channel):
    state = GPIO.input(channel)
    GPIO.output(red, state)
    
def eventtwo (channel):
    state = GPIO.input(channel)
    GPIO.output(blue, state)
    
def eventthree (channel):
    state = GPIO.input(channel)
    GPIO.output(yellow, state)
    
def eventfour (channel):
    state = GPIO.input(channel)
    GPIO.output("P9_31", state)
    
#interupts to call the events to turn on and off the LEDs    
GPIO.add_event_detect(sone, GPIO.BOTH, callback=eventone)    
GPIO.add_event_detect(stwo, GPIO.BOTH, callback=eventtwo)
GPIO.add_event_detect(sthree, GPIO.BOTH, callback=eventthree)
GPIO.add_event_detect(sfour, GPIO.BOTH, callback=eventfour)

while True:
    time.sleep(0.5)
    
    