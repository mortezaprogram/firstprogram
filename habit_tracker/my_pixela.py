import requests
PIXELA_ENDPOINT="https://pixe.la/v1/users"

user_params={
    "token":"kjfhkrekjsfklejkf",
    "username":"morix",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=PIXELA_ENDPOINT,json=user_params)
# print(response.text)
graph_endpoint=f"{PIXELA_ENDPOINT}/{username}"