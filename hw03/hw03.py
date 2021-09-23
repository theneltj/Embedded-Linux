#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
import time
import I2C


i2c = I2C(freq = 400000)
while True:
    print("Temp1 = ,"+ i2c.readfrom(49, 3))