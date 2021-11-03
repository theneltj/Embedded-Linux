# HOMEWORK 8

## PWN Using GPIO
First run 
'''
config-pin P9_31 gpio
'''
Then run with 
'''
sudo make TARGET=GPIOPWM.pru
'''

## PWM Using PRUOUT
First run 
'''
config-pin P9_31 pruout
'''
Then run with 
'''
sudo make TARGET=PRUPWM.pru
'''