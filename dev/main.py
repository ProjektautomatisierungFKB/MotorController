from __future__ import annotations

from time import sleep

from gpiozero import Servo

servo = Servo(17)

while True:
    servo.min()
    sleep(2)
    servo.mid()
    sleep(2)
    servo.max()
    sleep(2)
