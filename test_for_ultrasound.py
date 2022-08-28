import time
import ultrasound_sensor
import RPi.GPIO as GPIO
try:
    ultrasound_sensor.setup(3,4)
    while True:
        print(ultrasound_sensor.distance())
finally:
    GPIO.cleanup()

