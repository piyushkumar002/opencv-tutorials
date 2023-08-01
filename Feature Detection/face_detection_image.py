import cv2
import numpy as np

# Process:
'''
1. Read image
2. Convert into grayscale so working becomes easy
3. Detect faces using haarcascade --> based on features --> return coordinates of faces --> (x,y,w,h)
4. Draw rectangles around faces
'''

img = cv2.imread(filename=r"mygal.jpg")
img = cv2.resize(img, dsize=(500, 510))

# defining my haarcascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# face detection
# scaleFactor --> to what scale/resolution the image should be taken to to detect the faces
# minNeighbors = min. number of facial features to consider for declating it as a face (more than 3 or 5 is preffered)
faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.2, minNeighbors=5)

print(faces)

# drawing rectangles on faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, pt1=(x, y), pt2=(x+w, y+h), thickness=2, color=(0, 255, 0))
    cv2.putText(img, text=f"face_({x},{y})_({x+w},{y+h})", org=(x-10, y-10), fontScale=0.9, color=(255, 255, 255), fontFace=cv2.FONT_HERSHEY_PLAIN, thickness=1)

cv2.imshow("My gal Pic", img)

cv2.waitKey(0)
cv2.destroyAllWindows()