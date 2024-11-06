import numpy as np
import cv2
grey_img=np.random.randint(0,255,size=(300,600,3))
isWritten=cv2.imwrite("D:/rah-310/feth.jpg",grey_img)
if isWritten:
    print('the image successfully saved')
    