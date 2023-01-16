# hugepackage
HBRS project huge package inspector


## Betriebsanleitung des Raspberrypi
Pi mit Strom versorgen

### WLAN des Pis erscheint automatisch in der Netzwerkliste nach dem Hochfahren:
```
Name: hugepackage
Pwd: hugePck!23
```
### Zugang über Linux Konsole:

ssh -X pi@192.168.2.5

siehe Screenshot:
![](https://github.com/linuxfanatiker/hugepackage/blob/master/screenshot_console.png)
Pi ip: 192.168.2.5
nun ist das default Passwort vom pi: raspberry

Die Dateien zur Paketerkennung befinden sich im hugepackage Ordner, die Erkennung beginnt automatisch durch folgendes [Skript](https://github.com/linuxfanatiker/hugepackage/blob/master/hugepackage%20-%20Complete/package_pi_fotoapparat_skripte/pi_paketerkennung.sh).

Jetzt kann über den Knopf die Kamera ausgelöst und die Erkennung gestartet werden. Mehrfaches auslösen ist möglich, dass vorherige Bild wird übeschrieben.

### Genereller Ablauf:

Foto mit 800x600 Auflösung und Beleuchtung wird aufgenommen. 

Das Featureskript "Platzhalter" wird aufgerufen, um die Anzahl der gelben Pixel zu zählen und die Position des Pakets festzustellen.

Durch eingabe von DEBUG wird angezeigt wie das Bild bearbeitet wird.

Um eine Fotoserie zu starten das [Skript](https://github.com/linuxfanatiker/hugepackage/blob/master/hugepackage%20-%20Complete/package_pi_fotoapparat_skripte/pi_testfoto_serie.sh) starten.

Der Speicherort der Fotos muss bei Ausführung angegeben werden.

Allgemein für die Bedienung: [Link](https://www.heise.de/tipps-tricks/Linux-Befehle-Die-20-wichtigsten-Kommandos-3843388.html) oder Suchmaschine
