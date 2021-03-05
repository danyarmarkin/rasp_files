import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
n = 1

while (True):
    n = int(input("n =  "))
    for i in range(n):
         GPIO.output(18, True)
         time.sleep(0.1)
         GPIO.output(18, False)
         time.sleep(0.2)
    time.sleep(0.3)
