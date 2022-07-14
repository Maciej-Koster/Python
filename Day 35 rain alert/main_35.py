import requests
from twilio.rest import Client
import keys

api_key = keys.openweather_api_key
latitude = "46.034431"
longitude = "4.072695"
account_sid = keys.twilio_account_sid
auth_token = keys.twilio_auth_token

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
hourly_weather = weather_data["hourly"][0:12]
it_will_rain = False


for item in hourly_weather:
    print(item["weather"][0]["id"])
    if item["weather"][0]["id"] < 700:
        it_will_rain = True

if it_will_rain is True:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body='Będzie dzisiaj padało. Niezapomnij wziąć parasola ☂',
            from_=keys.twilio_number,
            to=keys.my_number
            )
    print("sukces")
    print(message.status)