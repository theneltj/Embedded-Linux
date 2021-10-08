cd /sys/class/i2c-adapter/i2c-2
ls -ls
echo tmp101 0x49 > new_device
dmesg -H | tail -3
cd 2-0049/hwmon/hwmon0
cat temp1_input