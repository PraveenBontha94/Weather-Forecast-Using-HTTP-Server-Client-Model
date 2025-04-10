from http.server import BaseHTTPRequestHandler, HTTPServer
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import requests
import json

API_KEY = "your_openweather_api_key"

class WeatherRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/weather"):
            query = self.path.split("?")[1] if "?" in self.path else ""
            params = dict(param.split("=") for param in query.split("&") if "=" in param)
            city = params.get("city", "")

            if city:
                try:
                    # Get location and timezone
                    geolocation = Nominatim(user_agent="weather_http_server")
                    location = geolocation.geocode(city)
                    if not location:
                        raise ValueError("Invalid city name")

                    timezone_finder = TimezoneFinder()
                    timezone = timezone_finder.timezone_at(lng=location.longitude, lat=location.latitude)
                    home = pytz.timezone(timezone)
                    local_time = datetime.now(home).strftime("%I:%M %p")

                    # Fetch weather data
                    weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
                    response = requests.get(weather_api_url).json()

                    if response.get("cod") != 200:
                        raise ValueError("Error fetching weather data")

                    condition = response['weather'][0]['main']
                    description = response['weather'][0]['description']
                    temp = int(response['main']['temp'] - 273.15)
                    pressure = response['main']['pressure']
                    humidity = response['main']['humidity']
                    wind = response['wind']['speed']

                    weather_data = {
                        "city": city,
                        "local_time": local_time,
                        "condition": condition,
                        "description": description,
                        "temperature": temp,
                        "pressure": pressure,
                        "humidity": humidity,
                        "wind_speed": wind
                    }

                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(weather_data).encode())
                except Exception as e:
                    self.send_error(400, f"Error processing request: {str(e)}")
            else:
                self.send_error(400, "City parameter is missing")
        else:
            self.send_error(404, "Endpoint not found")

def run_server():
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, WeatherRequestHandler)
    print("Weather HTTP Server running on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
