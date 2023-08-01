import cv2
import numpy as np

img = cv2.imread(filename=r"mygal.jpg")

cv2.imshow("My gal Pic", img)

cv2.waitKey(0)
cv2.destroyAllWindows()