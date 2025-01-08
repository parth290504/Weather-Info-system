import requests

API_KEY="59555c48961254430194fb02cbb20927"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

def Get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # For Celsius; use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()


def process_weather_data(data):
    if data.get('cod') != 200:  # Check for errors
        return f"Error: {data.get('message', 'Unable to fetch data')}"

    city = data['name']
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    return (
        f"Weather in {city}:\n"
        f"Temperature: {temperature}°C\n"
        f"Description: {weather_description.capitalize()}\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_speed} m/s\n"
    )

def final():
    city = input("Enter city name: ")
    weather_data = Get_weather(city)
    weather_report = process_weather_data(weather_data)
    print(weather_report)

final()
while True:
    again = int(input("Do you want to know Weather of any other city? \n press 1 if yes \n press 2 if no"))
    if again == 1:
        final()


    elif again == 2:
        print("Thank you for using Parth weather information system")



