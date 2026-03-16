import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
num = 0
sleep_time = 0.2
down = 10
up = 9

def dec_to_bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GPIO.setup(leds, GPIO.OUT)
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

while True:
    if GPIO.input(up):
        num = num + 1
        print(num, dec_to_bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down):
        num -= 1
        print(num, dec_to_bin(num))
        time.sleep(sleep_time)
    if num >= 64:
        num = 0
    if num < 0:
        num = 0
    GPIO.output(leds, dec_to_bin(num))