import cv2 
import numpy as np
import pytesseract
import imutils

img = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\licence_plate.jpg")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
#gray , çap , sigma color , sigma space
filtered = cv2.bilateralFilter(gray,6,250,250)
edged = cv2.Canny(filtered,30,200)   #min max
#tree mod değeri , chain metod değeri gereksiz yerleri yok eder
contours = cv2.findContours(edges , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
#uygun contur değerleri yakala 
cnts = imutils.grab_contours(contours)
#sorted=sırala , alana göre sırala , tersten sırala , 0dan 10a kadar için
cnts = sorted(cnts,key=cv2.contourArea,reverse=True)[:10]
screen = None

for c in cnts:
    epsilon = 0.018*cv2.arcLength(c,True)
    approx =