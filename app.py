from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Replace 'your_api_key_here' with your actual OpenWeatherMap API key
API_KEY = 'your_api_key_here'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/get/what-is-weather', methods=['GET'])
def get_weather():
    city = 'Leuven'
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # to get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed']
        }
        return jsonify(weather_info)
    else:
        return jsonify({'error': 'Could not fetch weather data'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
