import cv2 as cv
import random

image = cv.imread('assets/sunset.jpg', cv.IMREAD_UNCHANGED)

print(image.shape)

# for i in range(100):
#     for j in range(image.shape[1]):
#         image[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

tag = image[100:200, 250:450]

image[250:350, 150:350] = tag

cv.imshow('Sunset', image)
cv.waitKey(0)
cv.destroyAllWindows()
