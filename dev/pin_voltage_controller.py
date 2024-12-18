from __future__ import annotations

from logger import logger


class PinVoltageController:
    """A class to control the voltage of an GPIO pin"""

    def __init__(self):
        self._pin = 0
        self._voltage = 0

    def assign_pin(self, pin):
        """Set the pin of the voltage controller"""
        self._pin = pin
        logger.debug(f'Assigned pin {pin}')

    def set_voltage(self, voltage):
        """Sets the voltage of the pin in V"""
        logger.debug(f'Set voltage of pin {self._pin} to {voltage}V')
        self._voltage = voltage


con = PinVoltageController()

con.assign_pin(1)

con.set_voltage(0.3)

# test