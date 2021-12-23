import cv2

#카메라 장치열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed")
    exit()

#카메라 사진 찍기
ret, frame = cap.read()
cv2.imshow('frame',frame)
cv2.waitKey(10000)
cv2.imwrite('output.jpg',frame)

cap.release()
cv2.destroyAllWindows()