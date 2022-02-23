import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 12.0456
MY_LNG = 21.0123
MY_EMAIL = "###########@######.com"
MY_PASSWORD = "###############"


def is_at_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if abs(float(MY_LAT) - iss_latitude) <= 5 and abs(float(MY_LNG) - iss_longitude <= 5):
        return True


def is_dark():
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

    time_now = datetime.now().hour
    if time_now <= sunrise and time_now >= sunset:
        return True


while True:
    time.sleep(60)
    if is_at_position() and is_dark():
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up\n\nThe ISS is above you in the sky."
            )
            connection.close()


