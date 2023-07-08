import requests
from datetime import datetime

APP_ID = "xxxxxx"
API_KEY = "xxxxxxxxxxxxxx"

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/xxxxxxxxxxxxxxxxxx/workoutPlans/workouts"
header = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

excercise_input = input("Tell me what excercise you did today? ")
query = {
    "query": excercise_input,
    "gender": "male",
    "weight_kg": "69",
    "height_cm": "180",
    "age": "40"
}

response = requests.post(
    url=endpoint, json=query, headers=header)
response.raise_for_status()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
result = response.json()

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

    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,

    )
