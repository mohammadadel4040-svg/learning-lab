# Week 11 - EU Capitals Weather Data Collector

import requests
import json
import time
from datetime import datetime


# EU CAPITALS DATA

EU_CAPITALS = [
    {"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
    {"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
    {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
    {"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
    {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"city": "Amsterdam", "country": "Netherlands", "lat": 52.3676, "lon": 4.9041},
    {"city": "Brussels", "country": "Belgium", "lat": 50.8503, "lon": 4.3517},
]



# FETCH WEATHER FROM API

def fetch_weather(lat, lon):

    url = "https://api.open-meteo.com/v1/forecast"

    today = datetime.now().strftime("%Y-%m-%d")

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation_probability,weathercode",
        "start_date": today,
        "end_date": today,
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print("API request failed:", e)
        return None



# PROCESS WEATHER DATA

def process_data(raw, city, country):

    if not raw:
        return None

    current = raw.get("current_weather", {})

    result = {
        "country": country,
        "coordinates": {
            "latitude": raw.get("latitude"),
            "longitude": raw.get("longitude")
        },
        "current_weather": current,
        "hourly_forecast": []
    }

    hourly = raw.get("hourly", {})

    if "time" in hourly:
        for i in range(len(hourly["time"])):
            result["hourly_forecast"].append({
                "time": hourly["time"][i],
                "temperature": hourly["temperature_2m"][i],
                "precipitation_probability":
                    hourly["precipitation_probability"][i],
                "weathercode": hourly["weathercode"][i]
            })

    return result


# COLLECT DATA FOR ALL CAPITALS

def collect_weather():

    all_weather = {}

    print("Collecting EU weather data...\n")

    for capital in EU_CAPITALS:

        city = capital["city"]
        print("Fetching:", city)

        raw_data = fetch_weather(
            capital["lat"],
            capital["lon"]
        )

        processed = process_data(
            raw_data,
            city,
            capital["country"]
        )

        if processed:
            all_weather[city] = processed

        # API rate limit protection
        time.sleep(1)

    return all_weather


# SAVE JSON FILE

def save_json(data):

    with open("eu_weather_data.json", "w",
              encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    print("\nWeather data saved successfully!")


# MAIN PROGRAM

def main():

    data = collect_weather()

    if data:
        save_json(data)
    else:
        print("No data collected.")


if __name__ == "__main__":
    main()
