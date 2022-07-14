import requests
from datetime import datetime
import keys

TOKEN = keys.pixie_token
USERNAME = "maciej"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
#
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_endpoint_pixel = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20.9"
}


# response = requests.post(url=graph_endpoint_pixel, json=pixel_config, headers=headers)
#
# print(response.text)