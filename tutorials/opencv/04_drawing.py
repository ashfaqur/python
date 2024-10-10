import mailcap

import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while True:
    success, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    image = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    image = cv2.line(image, (0, height), (width, 0), (0, 255, 0), 5)
    image = cv2.rectangle(image, (100, 100), (width - 100, height - 100), (128, 128, 128), 5)
    image = cv2.circle(image, (int(width / 2), int(height / 2)), 60, (0, 0, 255), 20)

    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(image, 'Hello World!', (10, height - 10), font, 1, (0, 0, 129), 5, cv2.LINE_AA)

    cv2.imshow('Frame', image)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
