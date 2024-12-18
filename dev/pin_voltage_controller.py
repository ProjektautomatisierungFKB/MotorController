import RPi.GPIO as GPIO
from time import sleep

# GPIO-Setup
MOTOR_PINS = [17, 27, 22, 23]
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PINS, GPIO.OUT)

# PWM-Setup
pwms = [GPIO.PWM(pin, 50) for pin in MOTOR_PINS]
for pwm in pwms:
    pwm.start(7.5)  # Neutralstellung

def start_motors():
    for pwm in pwms:
        pwm.ChangeDutyCycle(10)  # Motoren nach vorne bewegen

def stop_motors():
    for pwm in pwms:
        pwm.ChangeDutyCycle(7.5)  # Stop

try:
    print("Starte Motoren...")
    start_motors()
    while True:
        sleep(1)
except KeyboardInterrupt:
    stop_motors()
    GPIO.cleanup()
