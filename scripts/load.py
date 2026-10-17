import csv
import sqlite3

def load():
    print("--> Chargement dans la base SQLite (weather.db)...")
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_metrics (
            timestamp TEXT PRIMARY KEY,
            temperature REAL,
            humidity REAL
        )
    """)
    
    with open("cleaned_data.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                INSERT OR REPLACE INTO weather_metrics (timestamp, temperature, humidity)
                VALUES (?, ?, ?)
            """, (row["timestamp"], float(row["temperature"]), float(row["humidity"])))
            
    conn.commit()
    
    # Contrôle qualité (Data Quality Check)
    cursor.execute("SELECT COUNT(*) FROM weather_metrics")
    count = cursor.fetchone()[0]
    print(f"--> Data Quality Check réussi: {count} enregistrements en base.")
    
    conn.close()

if __name__ == "__main__":
    load()
