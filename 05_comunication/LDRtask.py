import spidev
import time
import RPi.GPIO as GPIO

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
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
try:
    while True:
        reading = analog_read(0)
        if reading <= 512:
          GPIO.output(LED_PIN, GPIO.HIGH)
          print("LED ON")
        elif reading > 512:
          GPIO.output(LED_PIN, GPIO.LOW)
          print("LED OFF")
          


        print("Reading = %d" % (reading))
        time.sleep(0.5)
finally:
    spi.close()