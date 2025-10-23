import requests
import RPi.GPIO as GPIO
import time

RELAY_PIN = 26  # Change if needed

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

API_URL = "http://192.168.114.61:8080/sensor"
state = GPIO.input(RELAY_PIN)
payload = {
    "sensor": "relay",
    "value": bool(state),
    "ts": time.strftime("%Y-%m-%dT%H:%M:%S")
}
requests.post(API_URL, json=payload)
print("Posted:", payload)
