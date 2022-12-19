import os

import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_KEY_API = os.getenv("TEQUILA_API_KEY")


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_KEY_API}
        query = {"term": city_name, "location_type": "city"}
        resp = requests.get(url=location_endpoint, headers=headers, params=query)
        result = resp.json()["locations"]
        iata_code = result[0]["code"]
        return iata_code
