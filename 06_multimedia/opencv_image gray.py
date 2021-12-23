import cv2

img = cv2.imread('IU.jpg')
img2 = cv2.resize(img,(1000,800))

edge = cv2.Canny(img,50,100)
edge2 = cv2.Canny(img,100,100)
edge3 = cv2.Canny(img,150,100)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('IU',img)
cv2.imshow('IU1',gray)
cv2.imshow('IU2',edge)
cv2.imshow('IU3',edge2)
cv2.imshow('IU4',edge3)

while True:
   if cv2.waitKey(0) == 13:
       break
cv2.imwrite('my image',gray)

cv2.destroyAllWindows()