import cv2
import numpy as np

star = cv2.imread(filename=r"star.jpg")

kernel = np.ones((3, 3))

# Gradient: Difference between Erosion and Dialation
gradient = cv2.morphologyEx(star, kernel=kernel, op=cv2.MORPH_GRADIENT)

# Top Hat: Difference between Original Image and Opening
# op=cv2.MORPH_TOPHAT

# Black Hat: Difference between Original Image and Closing
# op=cv2.MORPH_BLACKHAT

cv2.imshow("Gradient", gradient)
cv2.imshow("Original Image", star)

cv2.waitKey(0)
cv2.destroyAllWindows()