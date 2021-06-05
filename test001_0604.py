import cv2 as cv
img = cv.imread("C://Coding//lena.jpg")

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)