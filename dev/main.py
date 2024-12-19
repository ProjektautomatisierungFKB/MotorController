from __future__ import annotations

from time import sleep

from drive_controller import DriveController

WHEEL_PINS = [[27, 22],
              [17, 23]]

driver = DriveController(WHEEL_PINS)

while True:
    driver.forwards()
    sleep(10)
    driver.idle()
    sleep(5)
    driver.backwards()
    sleep(10)
