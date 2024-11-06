import cv2
image=cv2.imread("D:/rah-310/rr.jfif",cv2.IMREAD_COLOR)
image1=cv2.imread("D:/rah-310/rr2.jpg")
cv2.imshow("rah",image)
cv2.imshow("rahul",image1)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()