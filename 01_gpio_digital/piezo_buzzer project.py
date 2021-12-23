import RPi.GPIO as GPIO
import time


BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN,262)
pwm.start(10) #duty cycle (0~100)



melody = [391,391,440,440,391,391,329,391,391,329,329,293,293,293,391,391,440,440,391,391,329,391,329,293,329,246]
try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
        


finally:
    pwm.stop()
    GPIO.cleanup()

