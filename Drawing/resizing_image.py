import cv2

img = cv2.imread(filename=r"/Drawing/mygal.jpg")
print(img.shape)

# width = 200
# height = 500
# dimension = (width, height)
# img2 = cv2.resize(src=img, dsize=dimension)
# print(img2.shape)
# If I want to make the image 10% of width and 10% of height
# I can use fx and fy
# fx --> width and fy--> height
####################################################
img2 = cv2.resize(src=img, dsize=(0, 0), fx=0.1, fy=0.1)
print(img2.shape)
####################################################
cv2.imshow("My gal Pic Resized", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()