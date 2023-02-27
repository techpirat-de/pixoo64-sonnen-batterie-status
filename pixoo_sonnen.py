# Erstellt mit python 3.9.7
# Danke an https://github.com/SomethingWithComputers/pixoo er hat eine Library für das Pixoo64 Display geschrieben
from pixoo import  Pixoo
import time
import requests
import local_ip_pixoo
import local_ip_sonnen

#print(api_key.API_KEY)
print(local_ip_pixoo.Local_ip)
print(local_ip_sonnen.Local_ip)

# API Endpoint URL der Sonnen Batterie
base_url = 'http://'+local_ip_sonnen.Local_ip+'/api/v2/status'
r = requests.get(base_url)
events_date = r.json()

# Sende einen HTTP-GET-Aufruf an die API
response = requests.get(base_url)

# Überprüfe den Statuscode der Antwort
if response.status_code == 200:
    # Wenn der Aufruf erfolgreich war, gib den Inhalt der Antwort aus
    print(response.content)
else:
    # Wenn der Aufruf fehlgeschlagen ist, gib eine Fehlermeldung aus
    print("API-Aufruf fehlgeschlagen: Statuscode {}".format(response.status_code))

# Erstellen einer Funktion um den Display zu aktualisieren
def update_display():

    r = requests.get(base_url)
    events_date = r.json()

    erzeugung = events_date['Production_W']
    verbrauch = events_date['GridFeedIn_W']
    bezug = events_date['Consumption_W']
    batterie_leistung = events_date['USOC']
    betriebs_modus = events_date['OperatingMode']

    modus_mapping = {
        "10": "Time-of-Use",
        "2": "Eigenverbrauch"
    }

    betriebs_modus_text = modus_mapping.get(betriebs_modus, "Unbekannter Modus ({})".format(betriebs_modus))
    print("Erzeugung:  \n {} Watt".format(erzeugung))
    print("Netz Bezug:  \n {} Watt".format(verbrauch))
    print("Aktueller Verbrauch:  \n {} Watt".format(bezug))
    print("Batterie Ladestand: \n {}%".format(batterie_leistung))
    print("Betriebsmodus:  \n  {}".format(betriebs_modus_text))
    

    # Setze die endpunkt URL für das Pixoo Display
    pix = Pixoo(local_ip_pixoo.Local_ip, 64, True)

    # Zeige aktuelle Uhrzeit und gebe sie im deutschen Format aus
    now = time.localtime()
    print(time.strftime('%H:%M:%S', now))

    pix.push()
    # Setze den Hintergrund auf schwarz    
    pix.fill((0, 0, 0))
    # Setze das Hintergrundbild
    pix.draw_image('images/sonne.png')
    
    # Schreibe die Texte auf dem Display
    pix.draw_text('Sonnen', (3,  3), (  0,   255, 0))
    pix.draw_text('Batterie', (3,  9), (255,    255,    0))
    pix.draw_text(time.strftime('%d.%m %H:%M', now), (3,  28), (252,253,254))
    pix.draw_text(str(erzeugung) + ' kW Erzeugt', (3,  34), (0,255,0))
    pix.draw_text(str(verbrauch) + ' kW Netz', (3,  40), (255,0,0))
    pix.draw_text(str(bezug) + ' kW Verbr', (3,  46), (0,0,255))
    pix.draw_text(str(batterie_leistung) + ' % Ladung', (3,  52), (252,253,254))
    pix.draw_text(str(betriebs_modus_text), (3,  58), (252,253,254))
    # Zeige die Texte auf dem Display
    pix.push()
    # Schreibe die Laufschrift auf dem Display 
    #pix.send_text( '    Jede Stunde wird der Preis angepasst                    ' , (0, 32), (  0,   255, 0), 1, 0, 46,  75)
    # wiederholen alle 60 Sekunden die Funktion
    time.sleep(10)
    # Starte die Funktion erneut
    update_display()
update_display()
