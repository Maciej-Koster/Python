import requests
from flight_data import FlightData
from pprint import pprint
import keys

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = keys.TEQUILA_API_KEY

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        data = response.json() ##########
        # pprint(data) #########3
        try:
            data = response.json()["data"][0]
        except IndexError:
            # print(f"No flights found for {destination_city_code}.")
            # return None
##########-- dodany kod
            query["max_stopovers"] = 5
            # print(query)
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {destination_city_code}.")
                return None
        # pprint(data)
#########--- dodany kod

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][0]["local_departure"].split("T")[0]
        )
        if data["pnr_count"] == 5:
            flight_data.return_date = data["route"][5]["local_departure"].split("T")[0]
            flight_data.stop_overs = 2
            travel = f"{data['route'][0]['cityTo']} and {data['route'][1]['cityTo']}"
            flight_data.via_city = travel


        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data

# from datetime import datetime, timedelta
# tomorrow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
# ORIGIN_CITY_IATA = "LON"
#
#
# sprawdzenie = FlightSearch()
# essa = sprawdzenie.check_flights(
#     origin_city_code=ORIGIN_CITY_IATA,
#     destination_city_code="DPS",
#     from_time=tomorrow,
#     to_time=six_month_from_today
# )
# # pprint(essa.via_city)
