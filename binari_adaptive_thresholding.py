import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = "test.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# ------ Mean Adaptive Thresholding -------

mean_bin = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 10)

cv2.namedWindow('mean thresholding', cv2.WINDOW_NORMAL)
cv2.imshow('mean thresholding', mean_bin)


# ------ Gaussian Adaptive Thresholding -------

gaus_bin = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 10)

cv2.namedWindow('Gaus Thresholding', cv2.WINDOW_NORMAL)
cv2.imshow('Gaus Thresholding', gaus_bin)


cv2.waitKey(0)
cv2.destroyAllWindows()