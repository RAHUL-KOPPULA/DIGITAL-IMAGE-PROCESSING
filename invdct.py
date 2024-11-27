import cv2
import numpy as np
img=cv2.imread("D:/rah-310/sunfl.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dcting=cv2.dct(np.float32(gray),cv2.DCT_INVERSE)
idcting=cv2.idct(dcting)
idct=np.uint8(idcting)
cv2.imshow("original image",gray)
cv2.imshow("cosine transform",dcting)
cv2.imshow("inverse cosine transform",idct)
cv2.waitKey(0)
cv2.destroyAllWindows()