import requests
from datetime import datetime
import smtplib

MY_LAT = 52.229675
MY_LNG = 21.012230

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


def at_position():
    if abs(float(MY_LAT) - iss_latitude) <= 5 and abs(float(MY_LNG) - iss_longitude <= 5):
        return True
    else:
        return False


def is_dark():
    if time_now.hour < sunrise and time_now.hour > sunset:
        return True
    else:
        return False


def send_notif():
        if at_position() == True and is_dark == True:
            pass
        else:
            pass

at_position(MY_LAT, iss_latitude)
is_dark()



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



