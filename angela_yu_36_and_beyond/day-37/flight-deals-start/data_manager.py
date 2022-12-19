import os

import requests

SHEETY_PRICES_ENDPOINT = os.getenv("env_sheety_prices_endpoint")

class DataManager:
    def __init__(self):
        self.destinations = {}

    def get_destinations(self):
        resp = requests.get(SHEETY_PRICES_ENDPOINT)
        data = resp.json()
        self.destinations = data["prices"]
        return self.destinations

    def update_destination_codes(self):
        for city in self.destinations:
            nu_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            resp = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=nu_data
            )
            print(resp.text)
