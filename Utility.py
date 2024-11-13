import openai
from Configuration import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_response_from_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

import requests

WEATHER_API_KEY = 'd133cb4179ecf979e2a4266e653c9c01'

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"Weather in {city}: {weather}, {temp}°C"
    else:
        return "City not found."

def get_response(user_input):
    if "weather" in user_input.lower():
        city = user_input.split("weather in")[-1].strip()
        return get_weather(city)
    else:
        return get_response_from_gpt(user_input)

