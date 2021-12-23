from typing_extensions import final
import RPi.GPIO as GPIO
import time


PIR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN,GPIO.OUT)

time sleep(5)
print("PIR Ready")
try:
    while True:
        GPIO.input(PIR_PIN)
        if val == GPIO.HIGH:
            print("움직임 감지")
        else :
            print("움직임 없음")

        time sleep(0.1)
finally:
    GPIO.cleanup()
    print("cleanup and exit")

        
        