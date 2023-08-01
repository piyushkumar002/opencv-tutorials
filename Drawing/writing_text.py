import cv2

img = cv2.imread(filename=r"/Drawing/mygal.jpg")

# parameters
origin = (400, 400) # width * height
font_csale = 1
font_face = cv2.FONT_ITALIC
thickness = 2
line_type = cv2.LINE_AA
text = "My Love!! :D"
color = (0, 255, 0) # BGR

img = cv2.putText(img= img, color=color, org=origin, text=text, thickness=thickness, fontFace=font_face, fontScale=font_csale, lineType=line_type)

cv2.imshow("My gal Pic", img)

cv2.waitKey(0)
cv2.destroyAllWindows()