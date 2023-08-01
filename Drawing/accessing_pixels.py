import cv2

img = cv2.imread(filename=r"/Drawing/mygal.jpg")

# top corner dimensions
height = 100
width = 100

# printing image before changing pixels values of that 100 100 region
print(img[0:height, 0:width])

# accessing pixel
img[0:height, 0:width] = [42, 42, 139] # BGR format --> changing to brown

cv2.imshow("My gal Pic", img)


# printing image after changing pixels values of that 100 100 region
print(img[0:height, 0:width])

cv2.waitKey(0)
cv2.destroyAllWindows()