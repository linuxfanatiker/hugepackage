#!/bin/bash

FILENAME=$1
I=0
KEY=1

pigs modes 23 r
pigs modes 18 w
pigs w 18 0

while [ true ]; do
  while [ $KEY -ge 1 ]
  do
     KEY=`pigs r 23`
  done
  echo "Ausloeser gedrueckt"
  KEY=1
  pigs w 18 1
  raspistill -e png -o "$FILENAME/$I.png" -w 800 -h 600 -t 500 -awb fluorescent
  pigs w 18 0
  echo "$FILENAME_$I.png erstellt"
  kill $!
  gpicview "$FILENAME/$I.png" &
  I=$(( $I + 1 ))
done

