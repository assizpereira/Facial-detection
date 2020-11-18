## program to detect faces and check against a list of suspects.

import cv2
import sys

#cascPath = sys.argv[1]
#faceCascade = cv2.CascadeClassifier(cascPath)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#this will utilise this specific haar cascade for the computer vision.

video_capture = cv2.VideoCapture(0)
#This will capture the frames immediately from the webcam.


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()#reader install

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#this is responsible for the data recognition right from the value of the interpretor to the data flow rate right.

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
       # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
