import cv2
import numpy as np

img = cv2.imread(filename=r"mygal.jpg")

height, width = img.shape[0], img.shape[1]
# For shifting parameters: matrix, size of image

# For shifting we need a matrix in following form
matrix = np.float32([[1, 0, 50], [0, 1, 200]]) # [[1, 0, width], [0, 1, height]]

dsize = (width, height)

# shifting
shifted_img = cv2.warpAffine(src=img, dsize=dsize, M=matrix)

cv2.imshow("Shifted Image", shifted_img)

cv2.waitKey(0)
cv2.destroyAllWindows()