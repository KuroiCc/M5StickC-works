'''
Haar Cascade Face detection with OpenCV
    Based on tutorial by pythonprogramming.net
    Visit original post: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/  
Adapted by Marcelo Rovai - MJRoBot.org @ 7Feb2018
'''

import numpy as np  # noqa
import cv2
import time
from datetime import datetime
import os

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade_profile = cv2.CascadeClassifier('script/haarcascade_profileface.xml')
faceCascade_front = cv2.CascadeClassifier('script/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
# cap.set(3, 640)  # set Width
# cap.set(4, 480)  # set Height
width = 800
height = 450
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
scaleFactor_profile = 1.3
minNeighbors_profile = 5
minSize_profile = (20, 20)
offset = 30

# scaleFactor_front = 5
# minNeighbors_front = 5
# minSize_front = (20, 20)

path = "/home/pi/vscoder/image/{date}".format(
    date=datetime.now().strftime("%Y%m%d%H%M%s")
)
if not os.path.exists(path):
    os.mkdir(path)
path += "/%s.jpg"
id = 0

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    now = datetime.now()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    profile_faces = faceCascade_profile.detectMultiScale(
        gray,
        scaleFactor=scaleFactor_profile,
        minNeighbors=minNeighbors_profile,
        minSize=minSize_profile
    )
    profile_faces_opposite = faceCascade_profile.detectMultiScale(
        cv2.flip(gray, 1),
        scaleFactor=scaleFactor_profile,
        minNeighbors=minNeighbors_profile,
        minSize=minSize_profile
    )

    # front_face = faceCascade_front.detectMultiScale(
    #     gray,
    #     scaleFactor=scaleFactor_front,
    #     minNeighbors=minNeighbors_front,
    #     minSize=minSize_front
    # )

    # for (x, y, w, h) in front_face:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #     roi_gray = gray[y:y + h, x:x + w]
    #     roi_color = img[y:y + h, x:x + w]

    for (x, y, w, h) in profile_faces:
        # roi_gray = gray[y:y + h, x:x + w]
        x -= offset
        y -= offset
        w += offset * 2
        h += offset * 2
        roi_color = img[y:y + h, x:x + w]
        id += 1
        # cv2.imwrite(path % id, roi_color)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    for (x, y, w, h) in profile_faces_opposite:
        x = width - x - w
        x -= offset
        y -= offset
        w += offset * 2
        h += offset * 2
        # roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        id += 1
        # cv2.imwrite(path % id, roi_color)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

    # time.sleep(0.03)

cap.release()
cv2.destroyAllWindows()
