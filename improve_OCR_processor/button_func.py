import cv2
import numpy as np


def remove_shadow(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bg_blur = cv2.GaussianBlur(image, (55, 55), 0)
    normalized = cv2.divide(image, bg_blur, scale=255)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    top_hat = cv2.morphologyEx(normalized, cv2.MORPH_TOPHAT, kernel)
    bottom_hat = cv2.morphologyEx(normalized, cv2.MORPH_BLACKHAT, kernel)
    shadow_removed = cv2.add(normalized, top_hat)
    return cv2.subtract(shadow_removed, bottom_hat)


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_background(image):
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()

    mean_bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 15)
    mean_bin_inv = 255 - mean_bin
    contours, _ = cv2.findContours(mean_bin_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        filtered_image = np.zeros_like(image)
        filtered_image[y:y + h, x:x + w] = image[y:y + h, x:x + w]
        return filtered_image
    return image


def clahe(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(3, 3))
    return clahe.apply(gray)


def prewitt(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
    prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
    prewitt_edges_x = cv2.filter2D(gray, -1, prewitt_x)
    prewitt_edges_y = cv2.filter2D(gray, -1, prewitt_y)
    prewitt_edges = cv2.magnitude(prewitt_edges_x, prewitt_edges_y)
    return cv2.normalize(prewitt_edges, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)


def sobel(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)
    sobel_edges_x = cv2.filter2D(gray, -1, sobel_x)
    sobel_edges_y = cv2.filter2D(gray, -1, sobel_y)
    sobel_edges = cv2.magnitude(sobel_edges_x, sobel_edges_y)
    return cv2.normalize(sobel_edges, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)


def contour(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean_bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 15)
    mean_bin_inv = 255 - mean_bin
    text_contours, _ = cv2.findContours(mean_bin_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered_image = np.zeros_like(gray)
    cv2.drawContours(filtered_image, text_contours, -1, (255, 255, 255), 1)
    return filtered_image


def mean_thresh(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 15)


def gauss_thresh(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 15)


def morph_open(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3, 3), np.uint8)
    return cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)


def morph_close(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3, 3), np.uint8)
    return cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)


def top_hat(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bg_blur = cv2.GaussianBlur(gray, (55, 55), 0)  # 가우시안 필터
    normalized = cv2.divide(gray, bg_blur, scale=255)  # 정규화
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))  # 텍스트 크기 10 by 10
    return cv2.morphologyEx(normalized, cv2.MORPH_TOPHAT, kernel)


def bottom_hat(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bg_blur = cv2.GaussianBlur(gray, (55, 55), 0)  # 가우시안 필터
    normalized = cv2.divide(gray, bg_blur, scale=255)  # 정규화
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))  # 텍스트 크기 10 by 10
    return cv2.morphologyEx(normalized, cv2.MORPH_BLACKHAT, kernel)