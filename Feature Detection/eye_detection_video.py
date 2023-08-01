import cv2
import numpy as np

# Process:
'''
1. The process is same only we'll read video as frames in a loop
2. Convert frames into grayscale so working becomes easy
3. Detect faces using haarcascade --> based on features --> return coordinates of faces --> (x,y,w,h)
4. Draw rectangles around faces in the frames
'''
# 0 - default webcam
# 1 - ext. webcam
# path - video file path
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(filename=r"funny_test_video.mp4")

# defining my haarcascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, dsize=(500, 700))

    # converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # face detection
    # scaleFactor --> to what scale/resolution the image should be taken to to detect the faces
    # minNeighbors = min. number of facial features to consider for declating it as a face (more than 3 or 5 is preffered)
    faces = face_cascade.detectMultiScale(image=frame, scaleFactor=1.2, minNeighbors=5)

    print(faces)

    # drawing rectangles on faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), thickness=2, color=(0, 255, 0))
        cv2.putText(frame, text=f"Face_({x},{y})_({x+w},{y+h})", org=(x-10, y-10), fontScale=0.9, color=(255, 255, 255), fontFace=cv2.FONT_HERSHEY_PLAIN, thickness=1)

        # roi = region of interest --> rectangle of face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(image=roi_gray, scaleFactor=1.2, minNeighbors=5)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, pt1=(ex, ey), pt2=(ex + ew, ey + eh), thickness=1, color=(0, 255, 0))

    cv2.imshow("Video Frame", frame)

    # Extra lines to remember
    if cv2.waitKey(40) & 0xFF==ord('q'):
        cap.release()
        break

cv2.destroyAllWindows()