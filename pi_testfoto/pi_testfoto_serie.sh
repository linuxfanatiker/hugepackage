#!/bin/bash

FILENAME=$1
I=0

while [ true ]; do
  raspistill -o ./$FILENAME_$I.png -w 800 -h 600 -t 1000
#  gpicview ./$FILENAME_$I.png
  I=$(( $I + 1 ))
done

