import json
import urllib.request

URL = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m,relative_humidity_2m"

def extract():
    print("--> Extraction des données depuis l'API Open-Meteo...")
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    
    with open("raw_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print("--> Données brutes sauvegardées dans raw_data.json")

if __name__ == "__main__":
    extract()
