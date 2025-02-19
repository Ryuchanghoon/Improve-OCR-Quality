import cv2
import numpy as np


image = cv2.imread("reduced_shadow.jpg", cv2.IMREAD_GRAYSCALE)


# ------ CLAHE -------

clahe = cv2.createCLAHE(clipLimit = 5.0, tileGridSize = (3, 3))
clahe_enhanced = clahe.apply(image)

cv2.namedWindow('CLAHE', cv2.WINDOW_NORMAL)
cv2.imshow('CLAHE', clahe_enhanced)

edges = cv2.Canny(clahe_enhanced, 50, 150)  # (하한선, 상한선)

cv2.namedWindow('Edge Canny', cv2.WINDOW_NORMAL)
cv2.imshow('Edge Canny', edges)


sobelx = cv2.Sobel(clahe_enhanced, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(clahe_enhanced, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobelx, sobely)
sobel_combined = np.uint8(sobel_combined)

cv2.namedWindow('Edge Sobel', cv2.WINDOW_NORMAL)
cv2.imshow('Edge Sobel', sobel_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()