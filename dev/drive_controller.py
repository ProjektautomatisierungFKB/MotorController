from __future__ import annotations

from logger import logger
from servo_controller import ServoController


class DriveController:
    """Class for handling driving"""

    def __init__(self, wheel_pins):
        self._front_left_servo = ServoController(wheel_pins[0][0])
        self._front_right_servo = ServoController(wheel_pins[0][1])
        self._back_left_servo = ServoController(wheel_pins[1][0])
        self._back_right_servo = ServoController(wheel_pins[1][1])

    def idle(self):
        """Stop all servos"""
        logger.debug('Idle movement')
        self._front_left_servo.idle()
        self._back_left_servo.idle()
        self._front_right_servo.idle()
        self._back_right_servo.idle()

    def forwards(self):
        """Drive forwards"""
        logger.debug('Moving forwards')
        self._front_left_servo.turn_counter_clockwise()
        self._back_left_servo.turn_counter_clockwise()
        self._front_right_servo.turn_clockwise()
        self._back_right_servo.turn_clockwise()

    def backwards(self):
        """Drive backwards"""
        logger.debug('Moving backwards')
        self._front_left_servo.turn_clockwise()
        self._back_left_servo.turn_clockwise()
        self._front_right_servo.turn_counter_clockwise()
        self._back_right_servo.turn_counter_clockwise()

    def left(self):
        """Drive left"""
        logger.debug('Moving left')
        self._front_left_servo.turn_counter_clockwise()
        self._back_left_servo.turn_counter_clockwise()
        self._front_right_servo.turn_counter_clockwise()
        self._back_right_servo.turn_counter_clockwise()

    def right(self):
        """Drive right"""
        logger.debug('Moving right')
        self._front_left_servo.turn_clockwise()
        self._back_left_servo.turn_clockwise()
        self._front_right_servo.turn_clockwise()
        self._back_right_servo.turn_clockwise()
