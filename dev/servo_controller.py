from __future__ import annotations

from gpiozero import Servo
from logger import logger


class ServoController:
    """Class to control a single servo"""

    def __init__(self, pin):
        self._pin = pin
        self._servo = Servo(pin)

    def idle(self):
        """Stops the servo"""
        self._servo.detach()
        logger.debug(f'Stopping servo on pin {self._pin}')

    def turn_clockwise(self):
        """Turns the servo clockwise"""
        self._servo.min()
        logger.debug(f'Turning servo on pin {self._pin} clockwise')

    def turn_counter_clockwise(self):
        self._servo.max()
        logger.debug(f'Turning servo on pin {self._pin} counter clockwise')
