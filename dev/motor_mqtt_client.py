from __future__ import annotations

from abstract_mqtt_client import AbstractMQTTClient
from drive_controller import DriveController
from logger import logger


class MotorMQTTClient(AbstractMQTTClient):

    publish_topics = []

    subscribe_topics = [
        'robotX/actuators/movement'
    ]

    def __init__(self, wheel_pins, publish_topics=publish_topics,
                 subscribe_topics=subscribe_topics):
        """Initialize the BluetoothMQTTClient"""
        super().__init__(publish_topics, subscribe_topics)

        self._driver = DriveController(wheel_pins)

    def handle_received_message(self, topic, payload):
        logger.info(f'Handling message on topic {topic}: {payload}')
        if (topic == 'robotX/actuators/movement'):
            if (payload == 'nil'):
                self._driver.idle()
            elif (payload == 'UP'):
                self._driver.forwards()
            elif (payload == 'DOWN'):
                self._driver.backwards()
            elif (payload == 'LEFT'):
                self._driver.left()
            elif (payload == 'RIGHT'):
                self._driver.right()
