import cv2

# Value of flags
# for reading image in color format without including alpha channel = 1, cv2.IMREAD_COLOR (by default)
# for reading image in grey scale = 0, cv2.IMREAD_GREYSCALE
# for reading image as it is including alpha channel = -1, cv2.IMREAD_UNCHANGED
# alpha channel is for transperancy .png files --> it has 4 channels unlike 3 in RGB

img = cv2.imread(filename=r"/Drawing/mygal.jpg", flags=0)
print(img.shape)
cv2.imshow("My gal Pic", img)

img2 = cv2.imread(filename=r"/Drawing/mygal.jpg", flags=1)
print(img2.shape)
cv2.imshow("My gal Pic", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()