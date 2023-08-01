import cv2

# shape of mygal is 828*818
img = cv2.imread(filename=r"/Drawing/mygal.jpg")

# lets draw a circle on the bob the builder
center1 = (400, 730) # width * height
radius1 = 60
color = (0, 255, 0) # BGR
thickness = 2

# drawing circle
cv2.circle(img=img, radius=radius1, center=center1, color=color, thickness=thickness, lineType=cv2.LINE_AA)

# drawing second bob the builder
center2 = (650, 700)
radius2 = 60
thickness2 = -1
cv2.circle(img=img, radius=radius2, center=center2, color=color, thickness=thickness2, lineType=cv2.LINE_AA)

cv2.imshow("My gal Pic", img)

cv2.waitKey(0)
cv2.destroyAllWindows()