import cv2
import numpy as np

img = np.zeros((500, 500))
cv2.rectangle(img, pt1=(50, 50), pt2=(400, 400), color=(255, 255, 255), thickness=-1)

cv2.imshow("Image with numpy", img)

cv2.waitKey(0)
cv2.destroyAllWindows()