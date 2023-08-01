import cv2
import numpy as np

img1 = cv2.imread(filename=r"mygal.jpg", flags=0)

kernel = np.ones((3, 3), np.int64)

img2 = cv2.morphologyEx(src=img1, op=cv2.MORPH_OPEN, kernel=kernel, iterations=2)
img3 = cv2.morphologyEx(src=img1, op=cv2.MORPH_CLOSE, kernel=kernel, iterations=2)

cv2.imshow("Opening", img2)
cv2.imshow("Original", img1)
cv2.imshow("closing", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()