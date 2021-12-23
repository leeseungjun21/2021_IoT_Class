import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 4 ## 초음파 발사핀 설정
ECHO_PIN = 14 ## 퍼진값을 다시받는 에코핀 설정
LED_PIN = 7 ## LED 핀
LED_PIN2 = 16
BUZZER_PIN = 8 ## 부저핀
SWITCH_PIN = 20 #스위치 핀

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN) ## 에코핀은 입력받는 값이기 때문에 setup을 input으로 설정 
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(LED_PIN2,GPIO.OUT)                    ## 나머지는 전부 output 설정
GPIO.setup(BUZZER_PIN,GPIO.OUT)
GPIO.setup(SWITCH_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
pwm = GPIO.PWM(BUZZER_PIN,7040) ## 부저의 주파수 값을 pwm에 넣어서 사용


        
try:
     while True:
        GPIO.output(LED_PIN2, GPIO.input(SWITCH_PIN)) ## GPIO 세팅
        GPIO.output(TRIGGER_PIN,GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIGGER_PIN,GPIO.LOW)
        while GPIO.input(ECHO_PIN) == 0: ## 발사
            pass
        start = time.time()


        while GPIO.input(ECHO_PIN) == 1: ##멈춘 시간까지
            pass
        stop = time.time()

        duration_time = stop - start ## 발사를 시작한 타임으로 끝나는 타임을 빼서 지속시간 계산
        distance = 17160 * duration_time ## 거리 계산 

        print('distance : %lfcm' % distance)
        if distance <= 100:
            GPIO.output(LED_PIN,GPIO.HIGH) ##  거리가  100 이하로 들어오면 울림
            pwm.start(10)
            print('led on')
        else:
            GPIO.output(LED_PIN,GPIO.LOW) ## 거리가 100 초과이면 꺼짐 
            print('led off')
            pwm.stop()
        time.sleep(0.1)



        
finally:
    GPIO.cleanup()
    print('cleanup and exit')

