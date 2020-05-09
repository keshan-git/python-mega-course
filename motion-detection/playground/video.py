import cv2
import time

video_capture = cv2.VideoCapture(0)
face_features = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    check, frame = video_capture.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Capturing', gray_img)
    # key = cv2.waitKey(1)

    faces = face_features.detectMultiScale(gray_img, scaleFactor=1.04, minNeighbors=5)

    for x, y, width, height in faces:
        frame = cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), thickness=1)

    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
video_capture.release()