import RPi.GPIO as GPIO
import time

GAS_PIN = 18  # Digital output pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_PIN, GPIO.IN)

print("Testing MQ5 Gas Sensor. Press Ctrl+C to exit.")
try:
    while True:
        status = GPIO.input(GAS_PIN)
        if status == 0:
            print("Gas Detected!")
        else:
            print("No Gas Detected")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
