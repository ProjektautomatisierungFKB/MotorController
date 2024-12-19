from __future__ import annotations

import time

from motor_mqtt_client import MotorMQTTClient
from mqtt_config import BROKER
from mqtt_config import PORT

WHEEL_PINS = [[27, 22],
              [17, 23]]

client = MotorMQTTClient(WHEEL_PINS)
client.connect(BROKER, PORT)
client.run(5)

while True:
    try:
        # keep main thread alive
        time.sleep(1)
    except KeyboardInterrupt:
        client.stop()
        exit()
