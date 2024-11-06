import cv2
import matplotlib.pyplot as plt
img = cv2.imread("D:/7032/Lenna_(test_image).png")
cv2.imshow("Color Image RGB",img)
imgrgb = cv2.cvt.Color(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()