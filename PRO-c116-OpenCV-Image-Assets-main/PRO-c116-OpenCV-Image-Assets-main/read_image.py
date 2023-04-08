import cv2
img=cv2.imread("butterflu.jpg")
cv2.imshow("Display Image" , img)
gray_img = cv2.cvtColor(img,cv2.COLOR.RGBRAY)
cv2.imshow("Grayscale", gray_img)
cv2.waitKey(0)