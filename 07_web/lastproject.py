import RPi.GPIO as GPIO
import spidev
import time
import cv2
import pyautogui

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

BUZZER_PIN = 4
LED_PIN = 5 
segments =  [22,25,12,13,14,15,16]
digits = [18,19,20,21]
switches = 26
SERVO_PIN = 2 #각각의 핀 번호를 변수에 저장

#spi 인스턴스 생성 
spi = spidev.SpiDev()
#spi 통신 시작
spi.open(0,0)

spi.max_speed_hz = 100000
#채널에서 읽어온 아날로그 값을 디지털 값으로 리턴하는 함수
def analog_read(channel):
  # [byte_1, byte_2, byte_3]
  # byte_1 : 1
  # byte_2 : channel(0) + 8 = 0000 1000 << 4 -> 1000 0000
  # byte_3 : 0
  ret = spi.xfer2([1, (channel + 8) << 4, 0])
  adc_out = ((ret[1] & 3) << 8) + ret[2]
  return adc_out



GPIO.setmode(GPIO.BCM) # 모드를 BCM번호로 사용하기 위해 BCM 모드로 전환

GPIO.setup(SERVO_PIN,GPIO.OUT) # SERVO를 잠금장치로 사용하므로 OUT 으로 설정

GPIO.setup(LED_PIN,GPIO.OUT) # LED는 경보기로 사용하므로 OUT 으로 설정

GPIO.setup(BUZZER_PIN,GPIO.OUT) # buzzer는 출력하는데 사용하므로 OUT 으로 설정

GPIO.setup(switches,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # 혹시 모를 쓰레기 값을 제거하기 위해 내부 풀업다운을 사용

for segment in segments:
    GPIO.setup(segment,GPIO.OUT) #4-digit FND는 출력하는데 사용하기에 OUT 으로 설정

for digit in digits:
    GPIO.setup(digit,GPIO.OUT) # 4-digit FND는 출력하는데 사용하기에 OUT 으로 설정

pwm_b = GPIO.PWM(BUZZER_PIN,1000) 
pwm_s = GPIO.PWM(SERVO_PIN,50) # pwm 인스턴트 생성과 주파수 설정
pwm_s.start(11) # 모터의 초기 값  설정

num =[[1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0],
    [1,1,0,1,1,0,1],        
    [1,1,1,1,0,0,1],
    [0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1],
    [1,0,1,1,1,1,1],
    [1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1],
    [0,0,0,0,0,0,0]] # 7segment의 각각 1,2,3..9 까지의 세팅값을 저장

def display(a,b): #4-digit FND에 숫자를 출력시키는 함수
    for i in range(len(digits)): #digit 의 개수만큼 반복
        if i + 1 == a: # 현재 차례가 4-digit FND에 표시하기 위에 함수에 입력한 칸과 같은지 확인
            GPIO.output(digits[i],GPIO.LOW) # 해당하는 핀을 LOW 로 설정
        else:
            GPIO.output(digits[i],GPIO.HIGH) # 해당하지 않는 핀을 HIGH 로 설정
    
    for j in range(len(segments)): # segment 의 개수만큼 반복
        GPIO.output(segments[j],num[b][j]) # 위쪽 num에 저장해논 세팅값을 4-digit FND 의 7segment에 출력시킴
    time.sleep(0.001) 

def setlock_value(a): #금고 해제를 위한 수치를 4-digits FND 에 표시하는 알고리즘
    display(1,int(a/1000)) #첫번째 자리 디스플레이
    display(2,int((a/100)%10)) #두번째 자리 디스플레이
    display(3,int((a/10)%10)) #세번째 자리 디스플레이
    display(4,int(a%10)) #네번째 자리 디스플레이

password = 11
open = 0
stack = 0.0
check = 0

while True:
    stack = stack + 0.01
    val = GPIO.input(switches)
    reading = analog_read(0)
    ch = reading/1023 * 50
    setlock_value(int(ch))

    ret, img = cap.read()
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('./xml/face.xml')

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        if val == 1 and stack > 1:
            print("1")
            if int(ch) == password and open == 0  and open != 2:
                open = 1 
                stack = 0
                pwm_s.ChangeDutyCycle(7)
            elif open == 1  and open != 2:
                open = 0
                stack = 0 
                pwm_s.ChangeDutyCycle(11)
            elif open == 2 and int(ch) == password:
                GPIO.output(LED_PIN, GPIO.LOW)
                pwm_b.stop()
                stack = 0
                open = 0
            elif open == 0:
                pwm_b.start(90)
                GPIO.output(LED_PIN, GPIO.HIGH)
                cv2.imwrite('fail.jpg',img)
                stack = 0
                open = 2
    
    cv2.imshow('frame',img)
    cv2.waitKey(0)
    pyautogui.press('y')
