import cv2
import numpy as np


image_path = "test.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

kernel = np.ones((3,3), np.uint8)  # 글씨 크기 고려 커널 사이즈 3


cv2.namedWindow('Origin', cv2.WINDOW_NORMAL)
cv2.imshow('Origin', image)


# ------ 모폴로지 열림 -------

opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.namedWindow('Opened', cv2.WINDOW_NORMAL)
cv2.imshow('Opened', opened)


# ------ 모폴로지 닫힘 -------

closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.namedWindow('Closed', cv2.WINDOW_NORMAL)
cv2.imshow('Closed', opened)


# ------ 모폴로지 열림 후 닫힘 -------

open_close = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
cv2.namedWindow('Close after Open', cv2.WINDOW_NORMAL)
cv2.imshow('Close after Open', open_close)


# ------ 모폴로지 닫힘 후 열림 -------

close_open = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
cv2.namedWindow('Open after Close', cv2.WINDOW_NORMAL)
cv2.imshow('Open after Close', close_open)


cv2.waitKey(0)
cv2.destroyAllWindows()