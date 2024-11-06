import cv2
import matplotlib.pyplot as plt
img=cv2.imread("D:/7090/5.png")
rgb=cv2.cvtColor(img.cv2.color_BGR2RGB)
plt.subplot(221),plt.imread(rgb),plt.title("original image"),plt.axis("off")

r,g,b=cv2.split(rgb)

plt.subplot(222),plt.imshow(rcmp='gray'),plt.title("red channel"),plt.axis("off")
plt.subplot(223),plt.imshow(g),plt.title("green channel"),plt.axis("off")
plt.subplot(223),plt.imshow(g),plt.title("blue channel"),plt.axis("off")