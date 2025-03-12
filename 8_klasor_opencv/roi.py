#ilgi alanına göre işlem yapılır

import cv2

img = cv2.imread("klon.jpg")

# istediğimiz alan yaklaşık olarak x ekseninde 30dan 200e kadar yde de 
roi = img[30:200, 200:400]


cv2.imshow("klon" , img)
cv2.imshow("ROI", roi)



cv2.waitKey(0)
cv2.destroyAllWindows()


