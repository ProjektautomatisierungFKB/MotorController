from __future__ import annotations

from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
from drive_controller import DriveController


@patch('drive_controller.ServoController')
def test_init(mock_servo_controller):
    wheel_pins = [[1, 2], [3, 4]]
    DriveController(wheel_pins)

    assert mock_servo_controller.call_count == 4
    mock_servo_controller.assert_any_call(1)
    mock_servo_controller.assert_any_call(2)
    mock_servo_controller.assert_any_call(3)
    mock_servo_controller.assert_any_call(4)


@pytest.fixture
def drive_controller_mocks():
    with patch('drive_controller.ServoController') as mock_servo_cls:
        mock_front_left = MagicMock(name='front_left')
        mock_front_right = MagicMock(name='front_right')
        mock_back_left = MagicMock(name='back_left')
        mock_back_right = MagicMock(name='back_right')

        mock_servo_cls.side_effect = [
            mock_front_left,
            mock_front_right,
            mock_back_left,
            mock_back_right
        ]

        wheel_pins = [[1, 2], [3, 4]]
        dc = DriveController(wheel_pins)

        return dc, mock_front_left, mock_front_right, mock_back_left, mock_back_right


def test_idle(drive_controller_mocks):
    dc, fl, fr, bl, br = drive_controller_mocks
    dc.idle()

    fl.idle.assert_called_once()
    fr.idle.assert_called_once()
    bl.idle.assert_called_once()
    br.idle.assert_called_once()


def test_forwards(drive_controller_mocks):
    dc, fl, fr, bl, br = drive_controller_mocks
    dc.forwards()

    fl.turn_counter_clockwise.assert_called_once()
    bl.turn_counter_clockwise.assert_called_once()
    fr.turn_clockwise.assert_called_once()
    br.turn_clockwise.assert_called_once()


def test_backwards(drive_controller_mocks):
    dc, fl, fr, bl, br = drive_controller_mocks
    dc.backwards()

    fl.turn_clockwise.assert_called_once()
    bl.turn_clockwise.assert_called_once()
    fr.turn_counter_clockwise.assert_called_once()
    br.turn_counter_clockwise.assert_called_once()


def test_left(drive_controller_mocks):
    dc, fl, fr, bl, br = drive_controller_mocks
    dc.left()

    fl.turn_clockwise.assert_called_once()
    bl.turn_counter_clockwise.assert_called_once()
    fr.turn_clockwise.assert_called_once()
    br.turn_counter_clockwise.assert_called_once()


def test_right(drive_controller_mocks):
    dc, fl, fr, bl, br = drive_controller_mocks
    dc.right()

    fl.turn_counter_clockwise.assert_called_once()
    bl.turn_clockwise.assert_called_once()
    fr.turn_counter_clockwise.assert_called_once()
    br.turn_clockwise.assert_called_once()


def test_turn_left(drive_controller_mocks):
    dc, fl, fr, bl, br = drive_controller_mocks
    dc.turn_left()

    fl.turn_counter_clockwise.assert_called_once()
    bl.turn_counter_clockwise.assert_called_once()
    fr.turn_counter_clockwise.assert_called_once()
    br.turn_counter_clockwise.assert_called_once()


def test_turn_right(drive_controller_mocks):
    dc, fl, fr, bl, br = drive_controller_mocks
    dc.turn_right()

    fl.turn_clockwise.assert_called_once()
    bl.turn_clockwise.assert_called_once()
    fr.turn_clockwise.assert_called_once()
    br.turn_clockwise.assert_called_once()
