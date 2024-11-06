import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("D:/rah-310/evil2.jfif")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
img=cv2.blur(img,(9,9))
plt.imshow(img)