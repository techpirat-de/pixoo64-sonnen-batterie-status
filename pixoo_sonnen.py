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
# speichern Sie die vorherigen Werte der Textfelder
previous_erzeugung = None
previous_verbrauch = None
previous_bezug = None
previous_batterie_leistung = None
previous_betriebs_modus_text = None

def update_display():
    global previous_erzeugung, previous_verbrauch, previous_bezug, previous_batterie_leistung, previous_betriebs_modus_text

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
    # Setze die endpunkt URL für das Pixoo Display
    pix = Pixoo(local_ip_pixoo.Local_ip, 64, True)
    now = time.localtime()

    # Setze den Hintergrund auf schwarz    
    pix.fill((0, 0, 0))
    # Setze das Hintergrundbild
    pix.draw_image('images/sonne.png')
    
    # Zeichne alle Texte neu
    pix.draw_text('Sonnen', (3,  3), (  0,   255, 0))
    pix.draw_text('Batterie', (3,  9), (255,    255,    0))
    pix.draw_text(time.strftime('%d.%m %H:%M', now), (3,  28), (252,253,254))
    pix.draw_text(str(erzeugung) + ' kW Erzeugt', (3,  34), (0,255,0))
    pix.draw_text(str(verbrauch) + ' kW Netz', (3,  40), (255,0,0))
    pix.draw_text(str(bezug) + ' kW Verbr', (3,  46), (0,0,255))
    pix.draw_text(str(batterie_leistung) + ' % Ladung', (3,  52), (252,253,254))
    pix.draw_text(str(betriebs_modus_text), (3,  58), (252,253,254))

    # Speichern Sie die aktuellen Werte der Textfelder
    previous_erzeugung = erzeugung
    previous_verbrauch = verbrauch
    previous_bezug = bezug
    previous_batterie_leistung = batterie_leistung
    previous_betriebs_modus_text = betriebs_modus_text

    # Zeigen Sie alle Texte auf dem Display an
    pix.push()

    # wiederholen alle 10 Sekunden die Funktion
    time.sleep(10)
    # Starte die Funktion erneut
    update_display()


update_display()
