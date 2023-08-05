

import requests
from datetime import datetime
PIXELA_ENDPOINT="https://pixe.la/v1/users"
USERNAME="morix"
TOKEN="kjfhkrekjsfklejkf"
GRAPH_ID="programgraph"

graph_endpoint=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
graph_config={
    "id": GRAPH_ID,
    "name": "Python_hours",
    "unit": "Hour",
    "type":"float",
    "color": "sora"
}
headers={
    "X-USER-TOKEN":TOKEN
}
pixel_creation_endpoint=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime.now()
pixel_data={
    "date": today.strftime("%Y%m%d"),
    "quantity": "20"
}

update_endpoint=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data={
    "quantity": "30"
}
# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)
delete_endpoint=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response=requests.delete(url=delete_endpoint ,headers=headers)
# print(response.text)