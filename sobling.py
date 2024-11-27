import cv2
import matplotlib.pyplot as plt
img=cv2.imread("D:/rah-310/OIP.jfif")
rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
gray=cv2.cvtColor(rgb_img,cv2.COLOR_BGR2GRAY)
img=cv2.GaussianBlur(gray,(3,3),0)
soblex=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobley=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=7)
plt.imshow(soblex)
plt.title("sobel-x edge detection")
plt.imshow(sobley)
plt.title("sobel-y edge detection")
