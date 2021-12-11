'''
Haar Cascade Face detection with OpenCV
    Based on tutorial by pythonprogramming.net
    Visit original post: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/  
Adapted by Marcelo Rovai - MJRoBot.org @ 7Feb2018
'''

import numpy as np  # noqa
import cv2
import time

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade_profile = cv2.CascadeClassifier('script/haarcascade_profileface.xml')
faceCascade_front = cv2.CascadeClassifier('script/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
# cap.set(3, 640)  # set Width
# cap.set(4, 480)  # set Height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    profile_faces = faceCascade_profile.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20)
    )
    profile_faces_opposite = faceCascade_profile.detectMultiScale(
        cv2.flip(gray, 1), scaleFactor=1.2, minNeighbors=5, minSize=(20, 20)
    )

    front_face = faceCascade_front.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20)
    )

    for (x, y, w, h) in front_face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    for (x, y, w, h) in profile_faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    for (x, y, w, h) in profile_faces_opposite:
        x = 1280 - x - w
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

    time.sleep(0.03)


cap.release()
cv2.destroyAllWindows()
