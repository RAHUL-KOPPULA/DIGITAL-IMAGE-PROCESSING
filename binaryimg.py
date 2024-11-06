import cv2
import matplotlib.pyplot as plt
image=cv2.imread("D:/rah-310/deer.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV_FULL)
plt.imshow(image)
grayimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(grayimg,cmap='gray')
(thresh,binary_image)=cv2.threshold(grayimg,100,100,
                                    cv2.THRESH_BINARY)
plt.imshow(binary_image,cmap='gray')