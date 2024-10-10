import cv2 as cv

img = cv.imread('assets/sample.jpg', cv.IMREAD_UNCHANGED)

img_show = cv.resize(img, (0,0), fx=0.1, fy=0.1)

img_rotate = cv.rotate(img_show, cv.ROTATE_90_CLOCKWISE)

cv.imwrite('assets/new_img.jpg', img_rotate)

# cv.imshow('Sample image',img_show)
cv.imshow('Sample image',img_rotate)
cv.waitKey(0)
cv.destroyAllWindows()




