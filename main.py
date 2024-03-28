import requests
from twilio.rest import Client
import os
API_KEY = YOUR_APIKEY
CITY = "Hyderabad, Telangana"
parameters = {
    "q":CITY,
    "appid":API_KEY,
    "cnt":4
}

account_sid = YOUR_ACCOUNT_SID
auth_token = YOUR_AUTH_TOKEN
client = Client(account_sid, auth_token)

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast",
                        params=parameters)
response.raise_for_status()
weather_codes = []
for _ in range(4):
    weather_codes.append(response.json()['list'][_]['weather'][0]['id'])
for weather_code in weather_codes:
    if weather_code < 700:
        message = client.messages.create(
            body="It's rainy day, don't forgot to bring an ☔",
            from_= TWILIO_MOBILE_NUMBER,
            to= TO_MOBILE_NUMBER
        )
        break
