import cv2

img = cv2.imread(filename=r"/Drawing/mygal.jpg")

height, width = img.shape[0], img.shape[1]

# parameters
center = (width//2, height//2) # width, height
axes = (150, 100) # width length, height length
rotation = 20
start_angle = 0
end_angle = 360 # drawing anti clockwise
thickness = -5
color = (0, 255, 255) # BGR

# drawing ellipse
cv2.ellipse(img=img, center=center, axes=axes, angle=rotation, startAngle = start_angle, endAngle=end_angle, color=color, thickness=thickness)

cv2.imshow("My gal Pic", img)

cv2.waitKey(0)
cv2.destroyAllWindows()