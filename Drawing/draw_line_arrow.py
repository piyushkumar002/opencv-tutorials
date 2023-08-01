import cv2

# shape of mygal is 828*818
img = cv2.imread(filename=r"/Drawing/mygal.jpg")

# lets draw a line across the bob the builder
point1 = (350, 800) # width * height
point2 = (650, 700)
color = (0, 255, 0) # BGR
thickness = 2
cv2.line(img=img, pt1=point1, pt2=point2, color=color, thickness=thickness)

# arrow function take the same arguments --> drawing random arrow
cv2.arrowedLine(img=img, pt1=(0,0), pt2=(400, 400), color=(0, 255, 255), thickness=thickness, tipLength=0.02)

cv2.imshow("My gal Pic", img)

cv2.waitKey(0)
cv2.destroyAllWindows()