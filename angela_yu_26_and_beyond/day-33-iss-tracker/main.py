from sqlite3 import paramstyle
import requests
from datetime import datetime

MY_LAT = 52.229675
MY_LNG = 21.012230

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# position = (float(longitude), float(latitude))

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = datetime.now()

print(time_now.hour)