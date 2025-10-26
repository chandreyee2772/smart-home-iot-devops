import BlynkLib, RPi.GPIO as GPIO
BLYNK_AUTH = "XiFF79IKOzkz7RzMx7D9TCIIy7Tmd-p4"
RELAY_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.handle_event("write V4")
def write_virtual_pin(pin, value):
    GPIO.output(RELAY_PIN, GPIO.HIGH if int(value[0]) else GPIO.LOW)

while True:
    blynk.run()
