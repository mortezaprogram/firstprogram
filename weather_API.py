import requests
MY_ENDPOINT="https://api.openweathermap.org/data/2.5/onecall"
api_key="dee2b5a42fe22308508701fe034f573c"
weathers_params={
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key
}
response=requests.get(MY_ENDPOINT,params=weathers_params)
print(response.status_code)