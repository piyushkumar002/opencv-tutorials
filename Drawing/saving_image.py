import cv2

img = cv2.imread(filename=r"/Drawing/mygal.jpg", flags=0)
print(img.shape)

width = 200
height = 500
dimension = (width, height)
img2 = cv2.resize(src=img, dsize=dimension)
print(img2.shape)


cv2.imshow("My gal Pic Resized", img2)

# for saving --> (path with image name can be any, which image)
cv2.imwrite(r"D:\styles\Programming\Open CV Python Tutorials\opencv-python\mygal_resized_grey.jpg", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()