import cv2
import matplotlib.pyplot as plt
img=cv2.imread("D:/rah-310/OIP.jfif")
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(gray,120,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(gray,120,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(gray,120,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(gray,120,255,cv2.THRESH_TOZERO_INV)
plt.subplot(331),plt.imshow(imgRGB,cmap='gray'),plt.title('Original image'),
plt.axis('off')
plt.subplot(332),plt.imshow(gray,cmap='gray'),plt.title('Gray Scale Image'),
plt.axis('off')
plt.subplot(333),plt.imshow(thresh1,cmap='gray'),plt.title('Binary Image'),plt.axis('off')
plt.subplot(334),plt.imshow(thresh2,cmap='gray'),plt.title('binary image invertede'),plt.axis('off')
plt.subplot(335),plt.imshow(thresh3,cmap='gray'),plt.title('truncate threshold'),plt.axis('off')
plt.subplot(336),plt.imshow(thresh4,cmap='gray'),plt.title('set to threshold'),plt.axis('off')
plt.subplot(337),plt.imshow(thresh5,cmap='gray'),plt.title('set to inverted'),plt.axis('off')

plt.show()