import json
import csv

def transform():
    print("--> Transformation des données...")
    with open("raw_data.json", "r") as f:
        data = json.load(f)
    
    hourly = data.get("hourly", {})
    times = hourly.get("time", [])
    temps = hourly.get("temperature_2m", [])
    humidities = hourly.get("relative_humidity_2m", [])
    
    cleaned_rows = []
    for t, temp, hum in zip(times, temps, humidities):
        # Filtre métier : conserver uniquement les relevés > 15°C
        if temp is not None and temp > 15.0:
            cleaned_rows.append({"timestamp": t, "temperature": temp, "humidity": hum})
            
    with open("cleaned_data.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "temperature", "humidity"])
        writer.writeheader()
        writer.writerows(cleaned_rows)
        
    print(f"--> {len(cleaned_rows)} lignes valides écrites dans cleaned_data.csv")

if __name__ == "__main__":
    transform()
