import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("D:/rah-310/lion22.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
fourier=cv2.dft(np.float32(gray),flags=cv2.DFT_COMPLEX_OUTPUT)
magnitude=20*np.log(cv2.magnitude(fourier[:,:,0],fourier[:,:,1]))
idft=cv2.idft(fourier)
imag=20*np.log(cv2.magnitude(idft[:,:,0],idft[:,:,1]))
imagnorm=cv2.normalize(imag,None,0,255,cv2.NORM_MINMAX,cv2.CV_8UC1)
cv2.imshow("original image",gray)
cv2.imshow("fourier transform",magnitude)
cv2.imshow("magnetic specturm",imagnorm)
cv2.waitKey(0)
cv2.destroyAllWindows()