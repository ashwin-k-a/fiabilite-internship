import cv2


srcBGR = cv2.imread("xyz.jpg")
destRGB = cv2.cvtColor(srcBGR,cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image',srcBGR)
cv2.waitKey(1)

cv2.imshow('rgbimage', destRGB)
cv2.waitKey(0)
cv2.destroyAllWindows()
