# Weather-Forecast-Using-HTTP-Server-Client-Model
# Weather Forecast Service Using HTTP Server-Client Model

## Developed by:
**B.V. Praveen (CS22B2033)**  
Indian Institute of Information Technology Design and Manufacturing, Kancheepuram

---

## Overview

This project implements a **client-server architecture in Python** to fetch and display real-time weather data using the [OpenWeather API](https://openweathermap.org/api). It demonstrates the fundamentals of HTTP-based communication, API integration, and basic socket programming.

---

## Aim

- Establish HTTP communication between a client and server.
- Integrate with the OpenWeather API to retrieve live weather data.
- Parse and present data such as temperature, humidity, wind speed, latitude, and longitude in a user-friendly format.

---

## System Design

### Architecture

[Client] --(city name)--> [Server] --(API Request)--> [OpenWeather API] ^ | |------(Weather Details)---------|


- **Client:** Sends a city name to the server.
- **Server:** Queries OpenWeather API and returns formatted weather data.

### Protocols & Concepts

- HTTP/1.1 based communication
- JSON data parsing
- Error handling for invalid city names and API issues

---

## Tools & Technologies

- **Language:** Python  
- **Libraries:** `socket`, `requests`, `json`, `logging`  
- **API:** OpenWeatherMap API

---

## How It Works

### Server

- Listens on TCP port `8080`
- Receives city name from the client
- Sends HTTP GET request to the OpenWeather API
- Parses and returns relevant weather details

### Client

- Connects to the server
- Sends city name
- Displays formatted weather information received from the server

---

## Error Handling

- Handles invalid city names, network errors, and API failures
- Logs errors using Python’s `logging` module

---

## Testing & Results

### Tested Scenarios:

- Valid city names (e.g., London, New York) → Correct data returned  
- Invalid city names (e.g., xyz123) → Graceful error handling  
- Network failure → Logs errors without crashing  

### Sample Output:

Client:
Enter city: London Temperature: 15°C Humidity: 72% Wind Speed: 5.2 m/s Coordinates: 51.51° N, -0.13° W

---

## Limitations

- Only supports single-word city names
- No support for concurrent clients

---

## Future Enhancements

- Multi-client support using threading/asynchronous programming
- Input validation for special characters/multi-word cities
- GUI integration using Tkinter
- Add advanced weather parameters like UV index or hourly forecast

---

## References

- [OpenWeatherMap API Docs](https://openweathermap.org/api)  
- [Python socket Library](https://docs.python.org/3/library/socket.html)  
- [Python requests Library](https://docs.python-requests.org/en/latest/)  
- *Computer Networking: Principles, Protocols, and Practice* by Olivier Bonaventure
