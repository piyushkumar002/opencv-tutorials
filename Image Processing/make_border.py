import cv2

img = cv2.imread(filename=r"star.jpg")

color_value = (255, 255, 0) # BGR

img = cv2.copyMakeBorder(img, top=100, bottom=100, left=100, right=100, borderType=cv2.BORDER_ISOLATED, value=color_value)

cv2.imshow("My gal Pic", img)

cv2.waitKey(0)
cv2.destroyAllWindows()