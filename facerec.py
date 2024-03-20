import threading

import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False

reference_img = cv2.imread('uglypic.jpg')

def check_face(frame):
    pass
while True:
    ret, frame = cap.read()
    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target = check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    cv2.destroyAllWindows()