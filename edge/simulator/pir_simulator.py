import time
import random
import requests

while True:
    motion = bool(random.getrandbits(1))
    ts = time.time()
    data = {"sensor": "pir", "value": motion, "ts": ts}
    requests.post("http://localhost:8080/sensor", json=data)
    print("Posted PIR:", motion)
    time.sleep(2)
