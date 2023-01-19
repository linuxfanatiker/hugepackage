#!/bin/bash

cd /home/pi/pck_shortcut
killall pigpiod
rm /tmp/log
touch /tmp/log
tail -f /tmp/log | ./lcd &

#FILENAME=$1
FILENAME='/tmp/paketerkennung.png'
DEBUG=$1
I=0
KEY=1

function display() {
	ZEILE1=$1
	ZEILE2=$2
	echo $ZEILE1 >>/tmp/log
	echo $ZEILE2 >>/tmp/log
}

pigs modes 23 r
pigs modes 18 w
pigs w 18 0

while [ true ]; do
  display "Taste druecken" "fuer Erkennung"
  while [ $KEY -ge 1 ]
  do
     KEY=`pigs r 23`
  done
  echo "Warte auf Ausloeser"
  echo "Ausloeser gedrueckt"
  KEY=1
  display "Erkennung laeuft" "Bitte warten"
# Beleuchtung einschalten
  pigs w 18 1
# Aufnahme starten
  raspistill -e png -o $FILENAME -w 800 -h 600 -t 500 -awb fluorescent
# Beleuchtung ausschalten
  pigs w 18 0
  echo "$FILENAME erstellt"
  echo "Jetzt dieses Bild verarbeiten"
  echo "Feature: Anzahl der gelben Pixel feststellen"
  IFS=','
# ggf umbenennen: feature_extraktion.py
  read -ra IMG_INFO <<< `python ./gelbanteil_feststellen.py $FILENAME`
  echo "DATEN $IMG_INFO"
  GELBEPIXEL=${IMG_INFO[0]}
  REIHE=${IMG_INFO[1]}
  UEBER_MAX=${IMG_INFO[2]}
  UNTER_MAX=${IMG_INFO[3]}
  echo "Gelbanteil ist $GELBEPIXEL"
  echo "Laenste Reihe ist $REIHE"
  echo "Erkennung laufen lassen"
  python ./mlp_inference_durchfuehren.py $GELBEPIXEL $REIHE $UEBER_MAX $UNTER_MAX
  PREDICTION=$?
  ERKANNT="Erkanntes Paket"
  if [ "$PREDICTION" == "1" ]; then
  	echo "Paketgroesse XS"
	PAKET="Paket XS"
  elif [ "$PREDICTION" == "2" ]; then
	echo "Paketgroesse S"
	PAKET="Paket S"
  elif [ "$PREDICTION" == "3" ]; then
	echo "Paketgroesse M"
	PAKET="Paket M"
  else
	echo "Es wurde kein gelbes Paket erkannt"
	ERKANNT="Es wurde kein"
	PAKET="Paket erkannt"
  fi

	display $ERKANNT $PAKET

	sleep 5

  if [ "$DEBUG" = "DEBUG" ]; then
  kill $!
  python ./gelbanteil_debug.py $FILENAME &
  fi
done

