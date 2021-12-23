import cv2

img = cv2.imread('IU.jpg')
img2 = cv2.resize(img,(1000,8000))

cv2.imshow('IU',img)
cv2.imshow('IU',img2)

cv2.waitKey(10000)

cv2.destroyAllWindows()