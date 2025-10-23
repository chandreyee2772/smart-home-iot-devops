import BlynkLib, RPi.GPIO as GPIO, time

BLYNK_AUTH = "<YOUR_BLYNK_TOKEN>"
MQ5_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ5_PIN, GPIO.IN)
blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.handle_event("read V2")
def read_virtual_pin_handler(pin):
    gas_detected = (GPIO.input(MQ5_PIN) == 0)
    blynk.virtual_write(2, int(gas_detected))  # V2 widget in Blynk

while True:
    blynk.run()
