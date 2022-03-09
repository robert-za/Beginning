import requests

api_key = "ba6bd56728af417906ed453ff9093106"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
MY_LONG = 21.01
MY_LAT = 52.23

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()