#!/bin/bash

FILENAME=$1
I=0
KEY=1

pigs modes 23 r

while [ true ]; do
  while [ $KEY -ge 1 ]
  do
     KEY=`pigs r 23`
  done
  echo "Ausloeser gedrueckt"
  KEY=1
  raspistill -o ./$FILENAME_$I.png -w 800 -h 600 -t 500
  echo "$FILENAME_$I.png erstellt"
  kill $!
  gpicview ./$FILENAME_$I.png &
  I=$(( $I + 1 ))
done

