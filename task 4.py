import requests
import json

def get_weather_data(user_input):
    api_key = 'YOUR_API_KEY'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    if user_input.isdigit():
        params = {'zip': user_input, 'appid': api_key}
    else:
        params = {'q': user_input, 'appid': api_key}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        print(f"Weather in {user_input}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("Error: Unable to retrieve weather data.")

if __name__ == "__main__":
    user_input = input("Enter a city name or zip code: ")
    get_weather_data(user_input)
