import cv2
import numpy as np


image = cv2.imread("reduced_shadow.jpg", cv2.IMREAD_GRAYSCALE)
image = image.astype(np.float32)

# ------ CLAHE -------

# clahe = cv2.createCLAHE(clipLimit = 5.0, tileGridSize = (3, 3))
# clahe_enhanced = clahe.apply(image)

# cv2.namedWindow('CLAHE', cv2.WINDOW_NORMAL)
# cv2.imshow('CLAHE', clahe_enhanced)


# ------ Prewitt Operator -------

Prewitt_detector_gy = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
], dtype=np.float32)

Prewitt_detector_gx = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=np.float32)

prewitt_edges_x = cv2.filter2D(image, -1, Prewitt_detector_gy)
prewitt_edges_y = cv2.filter2D(image, -1, Prewitt_detector_gx)
prewitt_edges = cv2.magnitude(prewitt_edges_x, prewitt_edges_y)

prewitt_edges = cv2.normalize(prewitt_edges, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

cv2.namedWindow('Prewitt detection', cv2.WINDOW_NORMAL)
cv2.imshow('Prewitt detection', prewitt_edges)


# ------ Sobel Operator -------

Sobel_detector_gy = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
], dtype=np.float32)

Sobel_detector_gx = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=np.float32)

sobel_edges_x = cv2.filter2D(image, -1, Sobel_detector_gy)
sobel_edges_y = cv2.filter2D(image, -1, Sobel_detector_gx)
sobel_edges = cv2.magnitude(sobel_edges_x, sobel_edges_y)

sobel_edges = cv2.normalize(sobel_edges, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

cv2.namedWindow('Sobel detection', cv2.WINDOW_NORMAL)
cv2.imshow('Sobel detection', sobel_edges)


cv2.waitKey(0)
cv2.destroyAllWindows()