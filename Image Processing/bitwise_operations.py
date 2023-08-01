import cv2

img1 = cv2.imread(filename=r"circle.jpg")
img2 = cv2.imread(filename=r"star.jpg")

# bitwise_and: if both pixel value is > 0 then true
# bitwise_or: if either pixel value is > 0 then true
# bitwise_xor: if either pixel is > 0 then true, but not both
# bitwise_not: if 255 then 0 and vice versa

img2 = cv2.resize(img2, dsize=(720, 576))

result = cv2.bitwise_xor(img1, img2)

cv2.imshow("Result", result)
cv2.imshow("Circle", img1)
cv2.imshow("Star", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()