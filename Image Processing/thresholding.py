import cv2

img = cv2.imread(filename=r"mygal.jpg")

# Thresholding Types:
# THRESH_BINARY =>      pixel >= threshold = 255 : 0
# THRESH_BINARY_INV =>  pixel >= threshold = 0 : 255
# THRUSH_TRUNC =>       pixel >= threshold = threshold
# THRUSH_TOZERO =>      pixel <= threshold = 0 : pixel
# THRUSH_TOZERO_INV =>  pixel >= threshold = 0 : pixel

ret, thresh = cv2.threshold(src=img, thresh=200, maxval=255, type=cv2.THRESH_TOZERO)

cv2.imshow("My gal Pic", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# DOCS Link: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html