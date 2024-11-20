import cv2
import numpy as np
in_img=cv2.imread("D:/rah-310/lion22.jpg")
kernel=np.ones((3,3),np.uint8)
eroded_img=cv2.erode(in_img,kernel,iterations=1)
cv2.imshow("input image",in_img)
cv2.imshow("eroded image",eroded_img)
dil_img=cv2.dilate(in_img,kernel,iterations=1)
cv2.imshow("dilated image",dil_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
