import cv2
image=cv2.imread("D:/rah-310/father.jpg",cv2.IMREAD_GRAYSCALE)
status=cv2.imwrite("D:/rah-310/father.jpg",image)
cv2.imshow("rah",image)
cv2.waitKey(100000)
print("image written in file system",status)
cv2.destroyAllWindows()