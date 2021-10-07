# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background black -fill green -font Times-Roman -pointsize 24 \
     -size $SIZE \
     label:'The BeagleBONE!\nBad to the Bone\nby Tyler Thenell' \
     -draw "text 0,200 'Bone Bone Bone'" \
     $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE