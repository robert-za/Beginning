import requests, os
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get("AUTH_TOKEN")

MY_LONG = 21.012230
MY_LAT = 52.229675

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily",
    "units": "metric"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()

condition_codes = []
for _ in range(11):
    condition_codes.append(int(weather_data["hourly"][_]["weather"][0]["id"]))

will_rain = False
for code in condition_codes:
    if code < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                .create(
                     body="Weź parasol. ☂️",
                     from_=os.environ.get('MY_FROM_NUMBER'),
                     to=os.environ.get('MY_NUMBER')
                 )
    print(message.status)