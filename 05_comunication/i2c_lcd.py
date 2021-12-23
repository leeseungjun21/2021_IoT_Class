from lcd import drivers
import time
import datetime 
import Adafruit_DHT

display = drivers.Lcd()
now = datetime.datetime.now()
sensor =  Adafruit_DHT.DHT11
DHT_PIN = 6
h,t = Adafruit_DHT.read_retry(sensor,DHT_PIN)


try:
    display.lcd_display_string("Hello, world!!",1)
    while True:
        display.lcd_display_string("** welcome **",2)
        time.sleep(2)
        display.lcd_display_string(" welcome ",2)
        time.sleep(2)
        display.lcd_display_string(now.strftime("%x %X"))
        time.sleep(2)
        if h is not None and t is not None:
            display.lcd_display_string('Temperatrue=%.1f* , Humidity=%.1f%%' % (t,h))
        else:
            display.lcd_display_string('Read Error')



finally:
    display.lcd_clear()
