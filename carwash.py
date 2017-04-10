# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:11:39 2017

@author: kilicm
"""


import json
import requests
import time

from datetime import date

# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("YOUR_SID", "YOUR_TOKEN")


weekday = date.today().isoweekday()
print(weekday)
if weekday == 5 or weekday == 6:
    
    def get_weather_json():
        req = requests.get('http://api.wunderground.com/api/{YOUR_KEY}/forecast/q/CA/San_Francisco.json')
        return req.json()

    def get_weather_info():
        weather_condition = []
        weather_city = get_weather_json()['forecast']['simpleforecast']['forecastday']
        for weather in weather_city:
            print(weather['conditions'])
            weather_condition.append(weather['conditions'])
    
        return weather_condition


    bad_condition= ['Chance of Flurries','Chance of Rain','Chance Rain',
                    'Chance of Freezing Rain','Chance of Sleet','Chance of Snow',
                    'Chance of Thunderstorms','Chance of a Thunderstorm','Unknown',
                    'Freezing Rain','Rain','Thunderstorms','Thunderstorm','Snow']
    def check_weather(forecast, bad_conditions):
        if any(weather in bad_condition for weather in forecast):
            print("No need to wash your car, weather is not good")
        else:
        
            print("Weather looks good for next 3 days and you should wash your")
            client.messages.create(to="+YOUR_NUMBER", from_="+YOUR_TWILIO_NUMBER",
                                   body="Perfect weather to wash your car")
            time.sleep(604800)

    check_weather(get_weather_info(), bad_condition)
    quit()
