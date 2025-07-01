import cv2

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 12)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.circle(frame, center=(frame.shape[1]//2, frame.shape[0]//2), radius=20, color=(0, 255, 0), thickness=-1)

    faces = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    print(faces)
    
    for i, (x, y, w, h) in enumerate(faces):
        # cv2.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), thickness=10, color=(0, 0, 255))
        cv2.circle(frame, center=(x+(w//2), y+(h//2)), radius=10, color=(255, 0,0), thickness=-1)
        cv2.putText(frame, text=f"Face {i+1} You are {abs(frame.shape[1]//2) - abs(x+int(w/2))} px away in Hz", org=(x, y), thickness=2, color=(255, 255, 255), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5)
        cv2.putText(frame, text=f"face {i+1} You are {abs(frame.shape[0]//2) - abs(y+int(h/2))} px away in Ver", org=(x,y-20), thickness=2, color=(255, 255, 255), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5)

    cv2.imshow("Live capture", frame)

    if cv2.waitKey(20) & 0xFF==ord("q"):
        cap.release()
        break

cv2.destroyAllWindows()