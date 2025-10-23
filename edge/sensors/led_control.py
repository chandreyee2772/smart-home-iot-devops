import BlynkLib, RPi.GPIO as GPIO

BLYNK_AUTH = "<YOUR_BLYNK_TOKEN>"
LED_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.handle_event("write V3")
def write_virtual_pin_handler(pin, value):
    if int(value[0]):
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

while True:
    blynk.run()
