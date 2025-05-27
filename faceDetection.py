import cv2
import cv2.data
import numpy as np


capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = capture.read()

    flip = cv2.flip(frame, 12)
    gray = cv2.cvtColor(flip, cv2.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=5)

    print(faces)
  
    for (x, y, w, h) in faces:
        cv2.rectangle(flip, pt1=(x-20,y-20), pt2=(x+w+20, y+h+20), thickness=4, color=(0, 0, 255))
        
    cv2.imshow("Face Detection Live", flip)
    

    if cv2.waitKey(20) & 0xFF==ord("q"):
        capture.release()
        break

cv2.destroyAllWindows()

