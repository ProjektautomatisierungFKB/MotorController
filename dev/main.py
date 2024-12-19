from __future__ import annotations

from time import sleep

from drive_controller import DriveController

WHEEL_PINS = [[27, 22],
              [17, 23]]

driver = DriveController(WHEEL_PINS)

while True:
    driver.forwards()
    sleep(5)
    driver.left()
    sleep(5)
    driver.right()
    sleep(5)
    driver.backwards()
    sleep(5)
