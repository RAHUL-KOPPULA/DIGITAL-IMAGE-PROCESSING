import cv2
import numpy as np
img=cv2.imread("D:/rah-310/cat.jpg")
kernel=np.ones((5,5),np.uint8)
dialtion=cv2.dilate(img,kernel,iterations=1)
cv2.imshow('original image',img)
cv2.imshow('dilation img',dialtion)         
cv2.waitKey(0)
cv2.destroyAllWindows()