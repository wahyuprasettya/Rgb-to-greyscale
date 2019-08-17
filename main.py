
import cv2

img = cv2.imread('wahyu.jpg', cv2.IMREAD_UNCHANGED)


scale_percent = 60
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
# asli = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

cv2.imshow('Gray image', gray)
# cv2.imshow('ORIGINAL image', asli)
cv2.waitKey(0)
cv2.destroyAllWindows()