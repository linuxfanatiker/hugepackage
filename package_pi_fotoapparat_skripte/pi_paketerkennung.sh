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
  echo "Warte auf Ausloeser"
  echo "Ausloeser gedrueckt"
  KEY=1
  pigs w 18 1
  raspistill -e png -o $FILENAME -w 800 -h 600 -t 500
  pigs w 18 0
  echo "$FILENAME erstellt"
  echo "Jetzt dieses Bild verarbeiten"
  echo "Feature: Anzahl der gelben Pixel feststellen"
  GELBEPIXEL=`python ./gelbanteil_feststellen.py $FILENAME`
  echo "Gelbanteil is $GELBEPIXEL"
  echo "Erkennung laufen lassen"
  python ./mlp_inference_durchfuehren.py $GELBEPIXEL
done

