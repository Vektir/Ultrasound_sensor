
import RPi.GPIO as GPIO
import time


trig = 0
echo = 0

def setup(trig1, echo1):
    trig = trig1
    echo = echo1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

def distance():
    if(trig == 0 or echo == 0):
        return -4
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)

    while GPIO.input(echo) == GPIO.LOW:
        t0 = time.time
    print(t0)
    while GPIO.input(echo) == GPIO.HIGH:
        t1 = time.time
    print(t1)
    distance = (t1-t0) * 343 * 100 / 2
    return distance





# trig = 3
# echo = 4

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(trig, GPIO.OUT)
# GPIO.setup(echo, GPIO.IN)
# distance(trig, echo)

