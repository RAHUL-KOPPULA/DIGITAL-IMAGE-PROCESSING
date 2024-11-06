import cv2
import matplotlib.pyplot as plt
img1=cv2.imread("D:/rah-310/deer.jpg")
cv2.imshow('Original image',img1)
cv2.waitKey(0)
Gaussian1=cv2.GaussianBlur(img1,(7,7),0)
cv2.imshow('Gaussian Blurring',Gaussian1)
cv2.waitKey(0)
Average1=cv2.blur(img1,(3,3))
plt.imshow(Average1)
cv2.waitKey(0)
cv2.destroyAllWindows()