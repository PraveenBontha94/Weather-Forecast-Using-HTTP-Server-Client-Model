import requests

def fetch_weather(city):
    try:
        url = f"http://localhost:8080/weather?city={city}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"City: {data['city']}")
            print(f"Local Time: {data['local_time']}")
            print(f"Condition: {data['condition']}")
            print(f"Description: {data['description']}")
            print(f"Temperature: {data['temperature']}°C")
            print(f"Pressure: {data['pressure']} hPa")
            print(f"Humidity: {data['humidity']}%")
            print(f"Wind Speed: {data['wind_speed']} m/s")
        else:
            print(f"Error: {response.status_code} - {response.reason}")
    except Exception as e:
        print(f"Failed to fetch weather: {e}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    fetch_weather(city_name)
