import RPi.GPIO as GPIO
import time
LED_PIN = 4
LED_PIN2 = 5
LED_PIN3 = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
for i in range(1):
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN, GPIO.LOW)
    print("led off")
    time.sleep(1)
    GPIO.output(LED_PIN2, GPIO.HIGH)
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN2, GPIO.LOW)
    print("led off")
    time.sleep(1)
    GPIO.output(LED_PIN3, GPIO.HIGH)
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN3, GPIO.LOW)
    print("led off")
    time.sleep(1)

GPIO.cleanup()