#!/bin/bash

#FILENAME=$1
FILENAME='/tmp/paketerkennung.png'
DEBUG=$1
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
# Beleuchtung einschalten
  pigs w 18 1
# Aufnahme starten
  raspistill -e png -o $FILENAME -w 800 -h 600 -t 500
# Beleuchtung ausschalten
  pigs w 18 0
  echo "$FILENAME erstellt"
  echo "Jetzt dieses Bild verarbeiten"
  echo "Feature: Anzahl der gelben Pixel feststellen"
  IFS=','
# ggf umbenennen: feature_extraktion.py
  read -ra IMG_INFO <<< `python ./gelbanteil_feststellen.py $FILENAME`
  GELBEPIXEL=${IMG_INFO[0]}
  REIHE=${IMG_INFO[1]}
  echo "Gelbanteil is $GELBEPIXEL"
  echo "Laenste Reihe ist $REIHE"
  echo "Erkennung laufen lassen"
  python ./mlp_inference_durchfuehren.py $GELBEPIXEL $REIHE
  PREDICTION=$?
  echo "Prediction ist $PREDICTION"
  if [ "$DEBUG" = "DEBUG" ]; then
  kill $!
  python ./gelbanteil_debug.py $FILENAME &
  fi
done

