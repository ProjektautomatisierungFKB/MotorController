from __future__ import annotations

import time

from drive_controller import DriveController
from logger import logger

WHEEL_PINS = [[27, 22],
              [17, 23]]

driver = DriveController(WHEEL_PINS)

try:
    driver.forwards()
    time.sleep(1)
    driver.backwards()
    time.sleep(2)
    driver.forwards()
    time.sleep(1)
    driver.left()
    time.sleep(1)
    driver.right()
    time.sleep(2)
    driver.left()
    time.sleep(1)
    driver.idle()
except KeyboardInterrupt:
    logger.info('Exiting...')
    exit()
