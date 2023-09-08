import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float

def get_lan_lon(city_name, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}').json()
    #print(resp)
    data = resp['coord']
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon
    #print(data)

def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=resp.get('main').get('temp')
    )
    return data

def main(city_name):
    lat, lon=get_lan_lon(city_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data


if __name__ == "__main__":
    lat, lon=get_lan_lon('Bhopal' , api_key)
    get_current_weather(lat, lon, api_key)