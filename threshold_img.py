import cv2
import numpy as np
def thres_finder(img, thres=20, delta_T=1.0):
    x_low, y_low = np.where(img <= thres)
    x_high, y_high = np.where(img > thres)
    mean_low = np.mean(img[x_low, y_low]) if len(x_low) > 0 else 0
    mean_high = np.mean(img[x_high, y_high]) if len(x_high) > 0 else 255
    new_thres = (mean_low + mean_high) / 2
    if abs(new_thres - thres) < delta_T:
        return new_thres
    else:
        return thres_finder(img, thres=new_thres, delta_T=delta_T)
img = cv2.imread("D:/rah-310/sunfl.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vv1 = thres_finder(gray_img, thres=30, delta_T=1.0)
ret, thresh = cv2.threshold(gray_img, vv1, 255, cv2.THRESH_BINARY)
out = cv2.hconcat([img, cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)])
cv2.imshow("Thresholded Image", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
