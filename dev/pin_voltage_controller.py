from __future__ import annotations


class PinVoltageController:
    """A class to control the voltage of an GPIO pin"""

    def __init__(self):
        self._pin = 0
        self._voltage = 0

    def assign_pin(self, pin):
        """Set the pin of the voltage controller"""
        self._pin = pin

    def set_voltage(self, voltage):
        """Sets the voltage of the pin"""
        self._voltage = voltage
