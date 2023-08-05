import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 167
AGE = 39

# YOUR_APP_ID="96cd9cd4"
# YOUR_API_KEY = "657a98bba45c67e4cd5f98908507ea85"

APP_ID = "96cd9cd4"
API_KEY = "657a98bba45c67e4cd5f98908507ea85"

exercise_endpoint= "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheet_endpoint="https://docs.google.com/spreadsheets/d/1TBL8v6xDsT1M0Xx7MxrgRWSiFXMSk2yomJ3wn0VT4d8/edit#gid=0"
sheet_endpoint="https://api.sheety.co/ef2606dcf3d0528e0df3d2931231a43c/myWorkouts01/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #No Auth
    bearer_headers = {
        "Authorization": "Bearer jkfhdflkfnhrf.wefnlhkhflefnerkikhs.lejfnerjilkaefmvoerjskjnvejlrk.sjh,jnve"
    }
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=bearer_headers)
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,auth=("mori","apitest@123"))
    print("hello")
    print(sheet_response.text)
