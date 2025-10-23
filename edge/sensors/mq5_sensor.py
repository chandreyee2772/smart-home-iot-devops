import requests
import RPi.GPIO as GPIO
import time

MQ5_PIN = 18  # Change if needed

GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ5_PIN, GPIO.IN)

API_URL = "http://192.168.114.61:8080/sensor"

while True:
    gas = GPIO.input(MQ5_PIN)
    payload = {
        "sensor": "mq5",
        "value": bool(gas == 0),  # Typically 0 means gas detected
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    try:
        requests.post(API_URL, json=payload)
        print("Posted:", payload)
    except Exception as e:
        print("Error posting:", e)
    time.sleep(2)
