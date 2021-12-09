import cv2
import sys

try:
    sys.argv[1]
except IndexError:
    print("ファイル名を入力してください")
    exit(0)

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
cv2.imshow('frame', frame)

key = cv2.waitKey(1)

path = "%s.jpg" % sys.argv[1]

cv2.imwrite(path, frame)

cap.release()
cv2.destroyAllWindows()
