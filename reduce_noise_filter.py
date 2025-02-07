import cv2
import numpy as np


image_path = 'test.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

mean_bin = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 15)  # Mean Adaptive Thresholding 이진화 기법

median_filter =cv2.medianBlur(mean_bin, 3)  # 3 by 3 필터
# 미디언 필터

bilater_filter = cv2.bilateralFilter(mean_bin, 9, 75, 75)  # (src, d, sigmaColor, sigmaSpace)
# 바이레이털 필터


cv2.namedWindow('origin', cv2.WINDOW_NORMAL)
cv2.imshow('origin', mean_bin)

cv2.namedWindow('median filter', cv2.WINDOW_NORMAL)
cv2.imshow('median filter', median_filter)

cv2.namedWindow('bilater_filter', cv2.WINDOW_NORMAL)
cv2.imshow('bilater_filter', bilater_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()