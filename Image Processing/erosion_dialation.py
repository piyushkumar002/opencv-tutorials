import cv2
import numpy as np

img1 = cv2.imread(filename=r"mygal.jpg", flags=0)

kernel = np.ones((3, 3), np.int64)

img2 = cv2.erode(src=img1, kernel=kernel, iterations=1)
img3 = cv2.dilate(src=img1, kernel=kernel, iterations=1)

cv2.imshow("erosion", img2)
cv2.imshow("Original", img1)
cv2.imshow("dialation", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()