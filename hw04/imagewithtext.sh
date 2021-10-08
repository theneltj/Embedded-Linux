# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

convert dog.jpg -gravity Center -pointsize 30 -annotate 0 'Dogo' temp1.jpg
sudo fbi -noverbose -T 1 temp1.jpg