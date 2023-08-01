import cv2
import numpy as np

img = cv2.imread(filename=r"lamborgini_love.jpg")

img = cv2.resize(img, dsize=(500, 500))

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Defining color range in hsv format
red_lower = np.array([1, 50, 50])
red_higher = np.array([25, 255, 255])

# create mask for red color
mask = cv2.inRange(hsv, red_lower, red_higher)

# result = cv2.bitwise_and(img, img, mask=mask)
result = cv2.bitwise_and(img, img, mask=mask)

# changing color of car to blue
result[mask > 0] = (170, 10, 10)
new_color_car = result

result = cv2.addWeighted(src1=img, alpha=1, src2=result, beta=1, gamma=0)

cv2.imshow("Car chassie", result)
cv2.imshow("Car", img)
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()