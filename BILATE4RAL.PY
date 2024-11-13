import cv2
import matplotlib.pyplot as plt
img=cv2.imread("D:/rah-310/hdbik.jpg")
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
bilimjg5=cv2.bilateralFilter(imgRGB,0,75,75)
bilimjg15=cv2.bilateralFilter(imgRGB,15,100,100)
plt.subplot(131), plt.imshow(imgRGB), plt.title('Original Image'), plt.axis('off')
plt.subplot(132), plt.imshow(bilimjg5), plt.title('bilimjg5'), plt.axis('off')
plt.subplot(133), plt.imshow(bilimjg15), plt.title('bilimjg15'), plt.axis('off')
