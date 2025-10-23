import requests
import RPi.GPIO as GPIO
import time

PIR_PIN = 17  # Change if needed

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

API_URL = "http://192.168.114.61:8080/sensor"

while True:
    motion = GPIO.input(PIR_PIN)
    payload = {
        "sensor": "pir",
        "value": bool(motion),
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    try:
        requests.post(API_URL, json=payload)
        print("Posted:", payload)
    except Exception as e:
        print("Error posting:", e)
    time.sleep(2)
