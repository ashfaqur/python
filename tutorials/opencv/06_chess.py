import numpy as np
import cv2

img = cv2.imread('assets/chess.jpg')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(img_grey, 100, 0.1, 10)
corners = np.int0(corners)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        x1, y1 = corners[i].ravel()
        x2, y2 = corners[j].ravel()
        x_diff = abs(x2 - x1)
        y_diff = abs(y2 - y1)
        if x_diff < 100 and y_diff < 100:
            color = tuple(map(lambda v: int(v), np.random.randint(0, 255, 3)))
            cv2.line(img, (x1, y1), (x2, y2), color, 2)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 10, (255, 0, 0), -1)

cv2.imshow('Chess', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
