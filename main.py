import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import json  # Import json for saving data to files

# Ensure the output directory exists
output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the environment variables from the .env file
load_dotenv()

# Load environment variables
WEATHERXMUSERNAME = os.getenv('WEATHERXMUSERNAME')
WEATHERXMPASSWORD = os.getenv('WEATHERXMPASSWORD')

# Base URL for the WeatherXM API
BASE_URL = 'https://api.weatherxm.com'

def login():
    """Authenticate with the WeatherXM API and return the access token."""
    url = f'{BASE_URL}/api/v1/auth/login'
    credentials = {
        "username": WEATHERXMUSERNAME,
        "password": WEATHERXMPASSWORD
    }
    response = requests.post(url, json=credentials)
    response.raise_for_status()
    return response.json()['token']

def get_devices(token):
    """Retrieve and return the list of devices."""
    url = f'{BASE_URL}/api/v1/me/devices'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_device_weather_history(token, device_id, from_date, to_date):
    """Retrieve weather data for a specific device."""
    url = f'{BASE_URL}/api/v1/me/devices/{device_id}/history'
    headers = {'Authorization': f'Bearer {token}'}
    params = {
        'fromDate': from_date,
        'toDate': to_date
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def save_weather_data(data, date):
    """Save weather data to a JSON file."""
    file_path = os.path.join(output_dir, f'{date}.json')
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Weather data saved to {file_path}")

if __name__ == '__main__':
    try:
        token = login()
        print("Authentication successful.")
        devices = get_devices(token)
        if devices:
            for device in devices:
                device_id = device['id']
                print(f"\nFetching weather history for device ID: {device_id}")
                from_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
                to_date = datetime.now().strftime('%Y-%m-%d')
                weather_data = get_device_weather_history(token, device_id, from_date, to_date)
                save_weather_data(weather_data, to_date)  # Save data to file
                
                # Print weather data in human-readable format
                for day_data in weather_data:
                    print(f"\nDate: {day_data['date']}, Time Zone: {day_data['tz']}")
                    for hourly_data in day_data.get('hourly', []):
                        print(f"Timestamp: {hourly_data['timestamp']}")
                        print(f"  Temperature: {hourly_data['temperature']}°C")
                        print(f"  Humidity: {hourly_data['humidity']}%")
                        print(f"  Feels Like: {hourly_data['feels_like']}°C")
                        print(f"  Wind Speed: {hourly_data['wind_speed']} km/h")
                        print(f"  Wind Direction: {hourly_data['wind_direction']} km/h")
                        print(f"  Wind Gust: {hourly_data['wind_gust']}")
                        print(f"  Precipitation: {hourly_data['precipitation']} mm")
                        print(f"  Precipitation Accumulated: {hourly_data['precipitation_accumulated']} mm")
                        print(f"  Pressure: {hourly_data['pressure']} hPa")
                        print(f"  Dew Point: {hourly_data['dew_point']}°C")
                        print(f"  UV Index: {hourly_data['uv_index']}")
                        print(f"  Illuminance: {hourly_data['illuminance']}")
                        print(f"  Solar Irradiance: {hourly_data['solar_irradiance']}")
                        print("  ---")
                
        else:
            print('No devices found.')
    except requests.RequestException as e:
        print(f'An error occurred: {e}')

