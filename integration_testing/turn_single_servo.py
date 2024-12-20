from __future__ import annotations

import time

from logger import logger
from servo_controller import ServoController

TEST_PIN = 27

servo = ServoController(TEST_PIN)

for _ in range(1, 5):
    try:
        servo.turn_clockwise()
        time.sleep(3)
        servo.idle()
        time.sleep(1)
        servo.turn_counter_clockwise()
        time.sleep(3)
    except KeyboardInterrupt:
        logger.info('Exiting...')
        exit()
