import picamera
import time

path = '/home/pi/src6/06_multimedia'

camera = picamera.PiCamera()
camera.resolution  = (640,480)
camera.start_preview()

while True:
    now_str = time.strftime("%Y%m%d_%H%M%S")
    val = input('photo : 1,video : 2,exit : 9 > ')
    if val == '1':
      camera.capture('%s/photo_%s.jpg' % (path,now_str))
    elif val == '2':
      camera.start_recording('%s/video_%s.h264' % (path,now_str))
      input('press enter to stop')
      camera.stop_recording()
    elif val == '9':
       camera.stop_preview()
       break
    else :
        print("에러")

