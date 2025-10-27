import time
import random
import requests

API_URL = 'http://localhost:8080/sensor'

while True:
    temp = round(random.uniform(18, 35), 1)   # Simulate 18–35°C
    hum = round(random.uniform(30, 70), 1)    # Simulate 30–70% humidity

    # Temperature
    data_temp = {
        'sensor': 'dht22_temp',
        'value': temp,
        'ts': time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    # Humidity
    data_hum = {
        'sensor': 'dht22_hum',
        'value': hum,
        'ts': time.strftime("%Y-%m-%dT%H:%M:%S")
    }

    print("Simulated Temp:", data_temp)
    print("Simulated Humidity:", data_hum)
    try:
        requests.post(API_URL, json=data_temp)
        requests.post(API_URL, json=data_hum)
    except Exception as e:
        print("POST failed:", e)
    time.sleep(2)
