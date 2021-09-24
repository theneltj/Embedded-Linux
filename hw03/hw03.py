#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus


bus = smbus.SMBus(2)    # Bus Number
address = 0x49          # Device address
address2 = 0x4a

while True:
    temp = bus.read_byte_data(address, 0) # 0 is register to read
    temp = temp * 9 / 5 + 32
    
    temp2 = bus.read_byte_data(address2, 0) # 0 is register to read
    temp2 = temp2 * 9 / 5 + 32
    
    print(chr(27)+"[2J")
    print("Temp1: ", temp, end="\n")
    print("Temp2: ", temp2, end="\n")
    
    time.sleep(0.25)
