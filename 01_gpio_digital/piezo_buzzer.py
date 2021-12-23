import RPi.GPIO as GPIO
import time


BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN,262)
pwm.start(100) #duty cycle (0~100)

time,sleep(2)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()
