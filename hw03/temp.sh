#!/bin/bash
while [ True ]  
do  
    temp=$(i2cget -y 2 0x49 0)
    temp1=$(($(($(($temp*9))/5))+32))
    
    temp2=$(i2cget -y 2 0x4a 0)
    temp3=$(($(($(($temp2*9))/5))+32))
echo "Sensor 1: "$temp1
echo "Sensor 2: "$temp3
done