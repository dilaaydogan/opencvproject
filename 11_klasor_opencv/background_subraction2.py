import cv2
import numpy as np

cap = cv2.VideoCapture("C:\\Users\\dila\\Desktop\\opencv.project\\input\\car.mp4")
subtractor = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=120,detectShadows=True)

while 1:
    _,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    mask = subtractor.apply(frame)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

    











    


    