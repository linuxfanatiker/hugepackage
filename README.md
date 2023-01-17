# hugepackage
HBRS project huge package inspector

## Idee
Die Idee ist es die Größe eines Paketes festzustellen, um das einsortieren an Paketstationen zu vereinfachen. Als einfachen Ansatz werden die Standard Pakete von DHL verwendet, diese sind zu einem großen Anteil gelb farbend. Folgend wurde eine Skript geschrieben das die Anzahl gelber Pixel erkennen kann. Je größer das Paket desto mehr Pixel können gezählt werden. Ein Problem was nun auftaucht ist, das bei größerer Entfernung des Pakets sich die Anzahl der Pixel verringert. Lösungsansatz dafür ist es die längste horizontale Linie zu finden, um herauszufinden in welcher Reihe sich diese befindet und somit die vertikale Position zu bestimmen.

## Betriebsanleitung des Raspberrypi
Pi mit Strom versorgen

WLAN des PIs erscheint automatisch in der Netzwerkliste nach dem Hochfahren:
```
Name: hugepackage
Pwd: hugePck!23
```
### Zugang über Linux Konsole:

ssh -X pi@192.168.2.5
```
Pi IP: 192.168.2.5
Neues Passwort: raspberry
```
siehe Screenshot:

![](https://github.com/linuxfanatiker/hugepackage/blob/master/screenshot_console.png)

Die Dateien zur Paketerkennung befinden sich im hugepackage Ordner, die Erkennung beginnt automatisch durch folgendes [Skript](https://github.com/linuxfanatiker/hugepackage/blob/master/hugepackage%20-%20Complete/package_pi_fotoapparat_skripte/pi_paketerkennung.sh).

Jetzt kann über den Knopf die Kamera ausgelöst und die Erkennung gestartet werden. Mehrfaches auslösen ist möglich, dass vorherige Bild wird übeschrieben.

### Genereller Ablauf:

Foto mit 800x600 Auflösung und Beleuchtung wird aufgenommen. 

Das [Featureskript](https://github.com/linuxfanatiker/hugepackage/blob/master/hugepackage%20-%20Complete/package_pi_fotoapparat_skripte/pi_paketerkennung.sh) wird aufgerufen, um die Anzahl der gelben Pixel zu zählen und die Position des Pakets festzustellen. Durch eingabe von DEBUG wird angezeigt wie das Bild bearbeitet wird.

Um eine Fotoserie zu starten, kann dieses [Skript](https://github.com/linuxfanatiker/hugepackage/blob/master/hugepackage%20-%20Complete/package_pi_fotoapparat_skripte/pi_testfoto_serie.sh) verwendet werden. Der Speicherort der Fotos wird durch das ablegen des Skripts im gleichen Ordner bestimmt.

Allgemein für die Bedienung: [Link](https://www.heise.de/tipps-tricks/Linux-Befehle-Die-20-wichtigsten-Kommandos-3843388.html) oder Suchmaschine
