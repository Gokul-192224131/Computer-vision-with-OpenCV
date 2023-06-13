import cv2 
import numpy as np

kernnal = np.array([[0,1,0],[-1,5,-1],[0,-1,0]])

img = cv2.imread("3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sharpened = cv2.filter2D(gray,-1,kernnal)
sharpened = cv2.multiply(sharpened,0.5)

cv2.imshow("sharpened",sharpened)
cv2.waitKey(0)
