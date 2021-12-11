import cv2
from datetime import datetime
# import sys

# try:
#     sys.argv[1]
# except IndexError:
#     print("ファイル名を入力してください")
#     exit(0)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while (True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    if key == ord('s'):
        path = "%s.jpg" % datetime.now()
        cv2.imwrite(path, frame)

cap.release()
cv2.destroyAllWindows()
