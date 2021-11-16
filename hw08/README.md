# HOMEWORK 8

## PWN Using GPIO
First run 
```
config-pin P9_31 gpio
```
Then run with 
```
sudo make TARGET=GPIOPWM.pru
```
See the file GPIOPWM.png to see the waveform.

1. The gpio pin can be toggled at 1.67 MHz
2. There is a fair amount of jitter and noise on the waveform.
3. The waveform is stable and the pwm is very symetric


## PWM Using PRUOUT
First run 
```
config-pin P9_31 pruout
```
Then run with 
```
sudo make TARGET=PRUPWM.pru
```
See the file PRUPWM.png to see the waveform.

1. The PRU PWM is not stable and the waveform has a large percent overshoot.
2. The standard deviation is about 20 MHz
3. The waveform doesnt have as much jitter as the gpio pin but is much more smooth with the overshoot

## Table of Results
|      | Freq (MHz) | Std Dev  | Jitter? | Stable? | Max Freq |
|------|------------|----------|---------|---------|----------|
| GPIO | 1.67       | 1.97 kHz | High    | Yes     | 1.67 MHz |
| PRU  | 50.64      | 20.0 MHz | Medium  | No      | 70 MHz   |

*The PRU output should be very stable.*

# hw08 grading

| Points      | Description |
| ----------- | ----------- |
| 14/14 | PRU
|  0/2 | Controlling the PWM Frequency - optional
|  0/2 | Reading an Input at Regular Intervals - optional
|  0/2 | Analog Wave Generator - optional
| 14/20 | **Total**

*My comments are in italics. --may*
