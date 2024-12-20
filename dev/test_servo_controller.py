from __future__ import annotations

from unittest.mock import patch

import pytest
from servo_controller import ServoController


@pytest.fixture
def mock_servo():
    with patch('servo_controller.Servo') as MockServo:
        mock_servo_instance = MockServo.return_value
        yield mock_servo_instance


def test_idle(mock_servo):
    pin = 17
    controller = ServoController(pin)

    controller.idle()

    mock_servo.detach.assert_called_once()


def test_turn_clockwise(mock_servo):
    pin = 17
    controller = ServoController(pin)

    controller.turn_clockwise()

    # Assert that min was called
    mock_servo.min.assert_called_once()


def test_turn_counter_clockwise(mock_servo):
    pin = 17
    controller = ServoController(pin)

    controller.turn_counter_clockwise()

    # Assert that max was called
    mock_servo.max.assert_called_once()
