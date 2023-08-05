import requests
from datetime import datetime

MY_LAT=51.507351
MY_LONG=-0.758127

my_param={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}
response=requests.get("https://api.sunrise-sunset.org/json",params=my_param)
response.raise_for_status()
data=response.json()
# print(data)
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
print(f"sunrise {sunrise}")
print(f"sunset  {sunset}")

time_now=datetime.now()
print(time_now)