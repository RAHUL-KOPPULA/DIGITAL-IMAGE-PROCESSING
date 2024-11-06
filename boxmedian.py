import cv2
import matplotlib.pyplot as plt
img=cv2.imread("D:/rah-310/feth.png")
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
ksize=(3,3)
k3blur=cv2.blur(imgRGB,ksize)
ksize=(5,5)
k5blur=cv2.blur(imgRGB,ksize)
ksize=(10,10)
k10blur=cv2.blur(imgRGB,ksize)
plt.subplot(221),plt.imshow(imgRGB),plt.title('original image'),plt.axis('off')
plt.subplot(222),plt.imshow(k3blur),plt.title('Blur (k=3*3)'),plt.axis('off')
plt.subplot(223),plt.imshow(k5blur),plt.title('Blur (k=5*5)'),plt.axis('off')
plt.subplot(224),plt.imshow(k10blur),plt.title('Blur (k=10*10)'),plt.axis('off')