import time
import random
import requests

API_URL = 'http://localhost:8080/sensor'

while True:
    mq_state = random.choice([0, 1])  # 1=gas detected, 0=no gas
    data = {
        'sensor': 'mq5',
        'value': mq_state,
        'ts': time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    print("Simulated Gas Detector:", data)
    try:
        requests.post(API_URL, json=data)
    except Exception as e:
        print("POST failed:", e)
    time.sleep(2)
