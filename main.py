import requests
from datetime import datetime

USER = "username"
TOKEN = "api token"

pixela_endpoint = "https://pixe.la/v1/users"

# create a user
user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=user_endpoint, json=user_params)
# print(response.text)

# create a graph
graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_config = {
    "id": "getting-up-early",
    "name": "Getting up early",
    "unit": "points",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# add a pixel to the graph
add_pixel_endpoint = f"{graph_endpoint}/getting-up-early"
today = datetime.now()

add_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50"
}

# response = requests.post(url=add_pixel_endpoint, json=add_pixel_config, headers=headers)
# print(response.text)

# update a pixel on the graph
update_pixel_endpoint = f"{add_pixel_endpoint}/20230614"
update_pixel_config = {
    "quantity": "40"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# delete a pixel
# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)