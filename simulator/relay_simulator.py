import time
import random
import requests

API_URL = 'http://localhost:8080/sensor'

while True:
    relay_state = random.choice([0, 1])
    data = {
        'sensor': 'relay',
        'value': relay_state,
        'ts': time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    print("Simulated Relay:", data)
    try:
        requests.post(API_URL, json=data)
    except Exception as e:
        print("POST failed:", e)
    time.sleep(2)
