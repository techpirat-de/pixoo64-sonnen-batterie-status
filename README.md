# pixoo64-tibber-preisanzeige
Diese Information richtet sich an alle Nutzer eine Sonnen Batterie oder an die, die eine erwerben wollen.

Die Idee ist, die aktuellen Batterie Daten auf dem Pixoo64 anzuzeigen ohne die App zu bemühen. 
Hast du noch keinen Pixoo64? Dann kannst du ihn hier kaufen: https://amzn.to/3X4DTJ8. 
Mein Code ist erstellt und getestet mit Python 3.9.7.

Getestet mit der sonnenBatterie 10 performance

Großer Dank an https://github.com/SomethingWithComputers/pixoo. 
Er hat eine Library für das Pixoo64 Display geschrieben, mit dessen Hilfe die Anzeige ganz leicht möglich ist. Ihr müsst die Library von "SomethingWithComputers" im gleichen Verzeichnis importieren.

Bitte folgende Module installieren und importieren:

from pixoo import Pixoo # Das ist die Library für das Pixoo64
import time
import requests
import local_ip_pixoo
import local_ip_sonnen

Um die Echtzeit-Anzeige zu bekommen, braucht ihr KEINEN API-Key von eurer Batterie.
Diesen braucht Ihr nur wenn Ihr z.B. den Betriebsmodus ändern möchtet.
Dazu müsst Ihr euch an dem lokalen Dashboard der Batterie als "User" anmelden und diesen unter "Software-Integration" erstellen
Das Passwort für den "User" steht ausen an der Sonnen-Batterie.

Ihr müsst auch die lokale IP-Adresse des Pixoo eintragen. Diese findet ihr über euren Router oder über die Pixoo Divoom App. In der App auf "Entdecken" unten links. Dann unter "Verfügbare Geräte" euren Pixoo64 auswählen und die "IP-Adresse" abschreiben. In meinem Fall ist es 192.168.2.200. Diese durch eure eigene in der Datei local_ip.py ersetzen.


Starte nun die pixoo_display.py in einer passenden python Umgebebung. 
Wie ihr diese Umgebung einrichtet zeige ich euch in einem Video https://youtu.be/zBce0U4HaOg
Nach dem Starten wird das Display alle 10 Sekunden aktualisiert. 
Bei ersten Start, startet das Display, in der Regel, einmal neu um in den Epfangmodus zu wechseln. 

Besucht mich auf YouTube: https://www.youtube.com/techpirat


##############################  

English version:
This information is intended for all users of a solar battery or those who want to purchase one.

The idea is to display the current battery data on the Pixoo64 without bothering the app.
Don't have a Pixoo64 yet? Then you can buy it here: https://amzn.to/3X4DTJ8.
My code is built and tested with Python 3.9.7.

Tested with the sonnenBatterie 10 performance

Big thanks to https://github.com/SomethingWithComputers/pixoo.
He has written a library for the Pixoo64 display that makes displaying it very easy. You have to import the library from "SomethingWithComputers" in the same directory.

Please install and import the following modules:

from pixoo import Pixoo # This is the library for the Pixoo64
import time
import requests
import local_ip_pixoo
import local_ip_suns

You do NOT need an API key from your battery to get the real-time display.
You only need this if you want to change the operating mode, for example.
To do this, you must log in to the battery's local dashboard as a "user" and create it under "Software Integration".
The password for the "user" is on the outside of the sun battery.

You must also enter the local IP address of the Pixoo. You can find this via your router or via the Pixoo Divoom app. In the app on "Discover" on the bottom left. Then select your Pixoo64 under "Available devices" and write down the "IP address". In my case it is 192.168.2.200. Replace this with your own in the local_ip.py file.


Now start the pixoo_display.py in a suitable python environment.
I show you how to set up this environment in a video https://youtu.be/zBce0U4HaOg
After starting, the display is updated every 10 seconds.
When first started, the display usually restarts once to switch to reception mode.

Visit me on YouTube: https://www.youtube.com/techpirat