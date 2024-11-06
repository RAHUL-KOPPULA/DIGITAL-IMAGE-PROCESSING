import cv2
c_img=cv2.imread("D:/rah-310/evil2.jfif")
g_img=cv2.imread("D:/rah-310/evil2.jfif",0)
cv2.imshow("evil image",c_img)
k=cv2.waitKey(0)
if k==ord('c'):
    cv2.imwrite("D:/rah-310/evil23.jfif",c_img)
    print("image saved in color")
    cv2.destroyAllWindows()
if(k==ord('g')):
     cv2.imwrite("D:/rah-310/evil24.jfif",g_img)
     print("image saved in gray colour")
     cv2.destroyAllWindows()