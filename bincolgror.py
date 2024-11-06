import cv2
import matplotlib.pyplot as plt
img=cv2.imread("D:/rah-310/tiger.jpg")
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,70,255,0)
plt.subplot(131),plt.imshow(imgRGB,cmap='gray'),plt.title('Original image'),
plt.axis('off')
plt.subplot(132),plt.imshow(gray,cmap='gray'),plt.title('Gray Scale Image'),
plt.axis('off')
plt.subplot(133),plt.imshow(thresh,cmap='gray'),plt.title('Binary Image'),plt.axis('off')
plt.show()