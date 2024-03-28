import requests
from twilio.rest import Client
import os
API_KEY = "76ed351edfc8000f97078f1f4c419ee2"
CITY = "Hyderabad,Telangana"
parameters = {
    "q":CITY,
    "appid":API_KEY,
    "cnt":4
}

account_sid = 'AC3eeb1bbcd63b613dc89ce26cbf9cda10'
auth_token = '13ef7044edbc12b3f61aee2e3c925f14'
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
            from_='+16107560774',
            to='+917569897932'
        )
        break
