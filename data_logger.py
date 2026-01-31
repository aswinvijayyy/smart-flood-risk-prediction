import csv
from datetime import datetime

def log_data(city, rainfall, drainage, risk_score, level):
    with open("flood_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now(), city, rainfall, drainage, risk_score, level
        ])
