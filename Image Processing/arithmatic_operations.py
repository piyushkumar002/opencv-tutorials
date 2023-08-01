import cv2

img1 = cv2.imread(filename=r"mygal.jpg")
img2 = cv2.imread(filename=r"test2.jpg")

# arithmetic operations possible
# add --> if > 255 then it'll make it 255
# result = cv2.add(img1, img2)

# subtact --> if < 0 or negative the it'll make it 0
# result = cv2.subtract(img1, img2)

# divide --> if decimal then round off as per mathematics (parameters: scale)
# result = cv2.divide(img1, img2, scale=50)

# addWeighted --> (parameters: src1, alpha, src2, beta, gamma)
# alpha = how much weight from 1st image
# beta = from the second image
# gamma = similar to scale but instead of multiplying every pixel, the gamma value is added to every pixel (how much bright)
# result = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=1, gamma=0)
# result = cv2.addWeighted(src1=img1, alpha=0.1, src2=img2, beta=0.1, gamma=100)
# result = cv2.addWeighted(src1=img1, alpha=0.1, src2=img2, beta=0.1, gamma=-10)

img2 = cv2.resize(src=img2, dsize=(828, 818))

result = cv2.addWeighted(src1=img1, alpha=0.1, src2=img2, beta=0.1, gamma=-10)

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

