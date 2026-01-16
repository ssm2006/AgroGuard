import requests
import json
from datetime import datetime

# Function to fetch weather data automatically
def get_weather_data(city):
    api_key = "YOUR_API_KEY_HERE"   # Replace with your API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        weather_info = {
            "City": city,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Pressure (hPa)": data["main"]["pressure"],
            "Weather Condition": data["weather"][0]["description"],
            "Wind Speed (m/s)": data["wind"]["speed"],
            "Date & Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return weather_info
    else:
        return "Error fetching weather data"


# Main execution
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    weather_data = get_weather_data(city_name)

    print("\n--- Automatic Weather Data ---")
    if isinstance(weather_data, dict):
        for key, value in weather_data.items():
            print(f"{key}: {value}")
    else:
        print(weather_data)
