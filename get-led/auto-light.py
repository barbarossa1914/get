import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 26
res = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(res, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(res))

