import cv2
import numpy as np

img = cv2.imread(filename=r"low-contrast-img.jpg", flags=0)
img = cv2.resize(src=img, dsize=(800, 500))

equilised_image = cv2.equalizeHist(img)

cv2.imshow("Original Image", img)
cv2.imshow("Equalized Image", equilised_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# After equalization, contrast of the image increases --> objects will be easily distinguishable
# difference between colors that helps us to distinguish between objects