#!/usr/bin/env python
import time

w1="/sys/class/hwmon/hwmon0/temp1_input"
w2="/sys/class/hwmon/hwmon1/temp1_input"
w3="/sys/class/hwmon/hwmon2/temp1_input"

while True:
    raw0 = open(w1, "r").read()
    raw1 = open(w2, "r").read()
    raw2 = open(w3, "r").read()
    print(chr(27)+"[2J")
    print "Temperature[0] is "+str(float(raw0.split("t=")[-1])/1000)+" degrees"
    print "Temperature[1] is "+str(float(raw1.split("t=")[-1])/1000)+" degrees"
    print "Temperature[2] is "+str(float(raw2.split("t=")[-1])/1000)+" degrees"
    time.sleep(0.3)
