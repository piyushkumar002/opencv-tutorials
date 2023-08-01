import cv2

img = cv2.imread(filename=r"/Drawing/mygal.jpg")

cv2.imshow("My gal Pic", img)

cv2.waitKey(0)
cv2.destroyAllWindows()