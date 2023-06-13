
import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)

img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7,7),0)
img_canny = cv2.Canny()

cv2.imshow("image", img_blur)




cv2.waitKey(0)


