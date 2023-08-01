import cv2
import numpy as np

img = cv2.imread(filename=r"mygal.jpg")

# pyrDown: keeps reducing the resolution to half everytime
# pyrUp: keeps making the resolution twice everytime

# fow down
for i in range(5):
    img = cv2.pyrDown(img)
    cv2.imshow("Downed Image", img)
    cv2.waitKey(0)

# For up
for i in range(5):
    img = cv2.pyrUp(img)
    cv2.imshow("Downed Image", img)
    cv2.waitKey(0)

# Observation: Took the smallest resolution and kept it increasing. Results will be
# different if we start with original img for up phase.

cv2.destroyAllWindows()