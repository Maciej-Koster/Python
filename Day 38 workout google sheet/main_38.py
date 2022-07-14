import requests
from datetime import datetime
import keys

GENDER = "male"
WEIGHT_KG = "85"
HEIGHT_CM = "180"
AGE = "27"

APP_ID = keys.nutritionix_app_id
API_KEY = keys.nutritionix_api_key
ENDPOINT_NUTRI = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHETTY_ENDPOINT = "https://api.sheety.co/6c633cceb2f0547e29ff5711c59c1108/workoutTracking/workouts"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# wysilek = input("Co dzisiaj robiłeś?").lower()
wysilek = "ran 3 miles"

params = {
    "query": wysilek,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=ENDPOINT_NUTRI, json=params, headers=header)
result = response.json()
# print(result)

execrise = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]
# print(execrise)

x = datetime.now()
data = x.strftime("%d/%m/%Y")
time = x.strftime("%H:%M:%S")

# date / TIME / EXECRISE / DURATION / CALORIES

google_params = {
    "workout": {
        "date": data,
        "time": time,
        "exercise": execrise,
        "duration": duration,
        "calories": calories
    }
}
header = {
    "Authorization": keys.sheety_auth
}


respone = requests.post(url=SHETTY_ENDPOINT, json=google_params, headers=header)
print(respone.text)