import cv2
import numpy as np


image = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)


# ------ CLAHE -------

clahe = cv2.createCLAHE(clipLimit = 5.0, tileGridSize = (3, 3))
clahe_enhanced = clahe.apply(image)

cv2.namedWindow('CLAHE', cv2.WINDOW_NORMAL)
cv2.imshow('CLAHE', clahe_enhanced)


# ------ Sharpening -------

sharpening_kernel = np.array([[-1, -1, -1], 
                              [-1,  9, -1], 
                              [-1, -1, -1]])

sharpened = cv2.filter2D(image, -1, sharpening_kernel)

cv2.namedWindow('Sharpening', cv2.WINDOW_NORMAL)
cv2.imshow('Sharpening', sharpened)


# ------ CLAHE 후 Sharpening -------

clahe_sharpen = cv2.filter2D(clahe_enhanced, -1, sharpening_kernel)

cv2.namedWindow('Sharpen after CLAHE', cv2.WINDOW_NORMAL)
cv2.imshow('Sharpen after CLAHE', clahe_sharpen)


# ------ Sharpening 후 CLAHE -------

sharpen_clahe = clahe.apply(sharpened)

cv2.namedWindow('CLAHE after Sharpen', cv2.WINDOW_NORMAL)
cv2.imshow('CLAHE after Sharpen', sharpen_clahe)


cv2.waitKey(0)
cv2.destroyAllWindows()