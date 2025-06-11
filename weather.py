import datetime
import json
import requests


def fetch_weather(latitude: float, longitude: float):
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=Asia%2FTokyo"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main():
    # Tokyo coordinates
    lat = 35.6895
    lon = 139.6917

    data = fetch_weather(lat, lon)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    output = {"timestamp": timestamp, "data": data}

    with open("weather.json", "w", encoding="utf-8") as fp:
        json.dump(output, fp, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
