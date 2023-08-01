import matplotlib.pyplot as plt
import cv2
import numpy as np

img = np.zeros((500, 500))
cv2.rectangle(img, pt1=(50, 50), pt2=(400, 400), color=(255, 255, 255), thickness=-1)

img2 = cv2.imread(filename=r"mygal.jpg", flags=0)

# Plotting the number of pixel intensity vs number of pixel corrs. to that intensity
plt.hist(img.ravel(), 256, [0, 256]) # requires max value and range, as max pixel value is 255 so 256 and range [0, 256]
plt.title("Image with numpy: pixels vs intensities")
cv2.imshow("Image with numpy", img)
plt.show()

plt.hist(img2.ravel(), 256, [0, 256]) # requires max value and range, as max pixel value is 255 so 256 and range [0, 256]
plt.title("My Gal Image: pixels vs intensities")
cv2.imshow("My Gal Image", img2)
plt.show()

# The above using the cv2 hist function
# channels --> BGR corrs. to 0, 1, 2
hist = cv2.calcHist(images=[img2], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.title("My Gal Image: pixels vs intensities using calcHist")
plt.plot(hist)
plt.show()

img3 = cv2.imread(filename=r"lamborgini_love.jpg", flags=1)
# we can split into 3 channels with following
b, g, r = cv2.split(img3)
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
cv2.imshow("Lamborgini Image with 3 channels", img3)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)
plt.title("BGR pixels vs intensities")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()