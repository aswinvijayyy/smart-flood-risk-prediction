import requests
from config import API_KEY

def get_rainfall(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    rainfall = data.get("rain", {}).get("1h", 0)
    return rainfall

if __name__ == "__main__":
    rain = get_rainfall(8.5241, 76.9366)
    print("Rainfall in last 1 hour:", rain, "mm")
