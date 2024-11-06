import cv2
img=cv2.imread("D:/rah-310/jerry.jpg",cv2.IMREAD_COLOR)
cv2.imshow("minni", img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
        cv2.imwrite("D:/rah-310/jerry1.jpg",img)
        cv2.destroyAllWindows()