import cv2

img = cv2.imread(filename=r"mygal.jpg")

# Default is BGR
# We can convert it in any color models like RGB, HSV, etc.

image = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)

cv2.imshow("My gal Pic", image)
cv2.waitKey(0)
cv2.destroyAllWindows()