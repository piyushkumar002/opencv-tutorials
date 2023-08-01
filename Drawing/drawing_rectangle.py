import cv2

img = cv2.imread(filename=r"mygal.jpg")

# parameters
start_point = (320, 40)
end_point = (600, 420)
thickness = 2
color = (0, 255, 0) # BGR

img = cv2.rectangle(img, pt1=start_point, pt2=end_point, thickness=thickness, color=color)


cv2.imshow("My gal Pic", img)

cv2.waitKey(0)
cv2.destroyAllWindows()