# Homework 2


## BUTTONS AND LEDS
### hw02.py

   Turns on LEDS when holding down the corresponding button

   Uses interupts to trigger the LED state change
    
## Speed Questions
1.)	3.7 V    -130 mV
2.)	16.8 Hz    T = 1/16.8 = 60 ms
3.)	It is not very close to 100 ms because it is based on the time it takes to run an instruction
4.)	They differ because the program is basing the period on instruction length
5.)	68%
6.)	The shortest value for the frequency is 25.5 Hz so T = 39.2 ms
0.1 ->  235 ms
0.01 -> 58 ms
0.001 -> 42 ms
0.0001 -> 39.3 ms
7.)	The period is very stable
8.)	Period is still stable
9.)	 Yes it can be slightly faster 
10.)	 Yes this can also help shorten the period
11.)	 34.3 ms is the shortest

### GPIO
|        | SH      | Python  | C       |
|--------|---------|---------|---------|
| MinV   | -130 mV | -130 mV | -250 mV |
| MaxV   | 3.7 V   | 3.6 V   | 3.81 V  |
| Freq   | 25.5 Hz | 412 Hz  | 3.2 KHz |
| Period | 39.3 ms | 2.4 ms  | 0.31 ms |
| HTOP   | 77%     | 15%     | 77%     |

### GPIOD
|        | Python    | C         |
|--------|-----------|-----------|
| MinV   | -80 mV    | -80 mV    |
| MaxV   | 3.98 V    | 3.98 V    |
| Freq   | 57 KHz    | 290 KHz   |
| Period | 0.017 ms  | 0.0034 ms |
| HTOP   | 100%      | 100%      |



## ETCH A SKETCH
# EtchSketch.py 

   Runs etch a sketch progam controlled by 4 push buttons
   
   Up P9_19
   Down P9_17
   Right P9_13
   Left P9_11
   
   Added clear screen and fixed bugs
   
   Added border as well
   
   Run program using ./EtchSketch.py and enter dimesions to begin etching
