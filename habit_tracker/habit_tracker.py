import requests
PIXELA_ENDPOINT="https://pixe.la/v1/users"
USERNAME="morix"
TOKEN="kjfhkrekjsfklejkf"

graph_endpoint=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
graph_config={
    "id": "programgraph",
    "name": "Python_hours",
    "unit": "Hour",
    "type":"float",
    "color": "sora"
}
headers={
    "X-USER-TOKEN":TOKEN
}

response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(response.text)
