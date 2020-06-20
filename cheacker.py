import numpy as np
import cv2
b=np.ones([640,640],dtype='uint8')*255
for i in range(80,640,80*2):
    for j in range(80,640,80*2):
        b[j-80:j,i-80:i]=0
        b[j:j+80,i:i+80]=0
cv2.imshow('checker board',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
