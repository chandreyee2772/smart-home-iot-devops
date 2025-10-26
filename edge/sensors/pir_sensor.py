import BlynkLib, RPi.GPIO as GPIO, time

BLYNK_AUTH = "XiFF79IKOzkz7RzMx7D9TCIIy7Tmd-p4"
PIR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.handle_event("read V1")
def read_virtual_pin_handler(pin):
    motion = GPIO.input(PIR_PIN)
    blynk.virtual_write(1, int(motion))  # V1 widget in Blynk Mobile/Web dashboard

while True:
    blynk.run()
