import RPi.GPIO as GPIO
import time

SWITCH_PIN = 12
SWITCH_PIN1 = 13
SWITCH_PIN2 = 15  
LED_PIN = 8
LED_PIN1 = 20
LED_PIN2 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN1,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.input(SWITCH_PIN))
        GPIO.output(LED_PIN1, GPIO.input(SWITCH_PIN1))
        GPIO.output(LED_PIN2, GPIO.input(SWITCH_PIN2))
finally:
    GPIO.cleanup()
    print('bye')
 