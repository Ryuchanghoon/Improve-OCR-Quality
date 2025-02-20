import cv2
import numpy as np


image = cv2.imread("reduced_shadow.jpg", cv2.IMREAD_GRAYSCALE)

mean_bin = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 15)  # Mean Adaptive Thresholding
mean_bin_inv = 255 - mean_bin  # 흑백 반전


# ------ 경계선 for Bounding Box -------

contours, _ = cv2.findContours(mean_bin_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest_contour)  # 좌표값 추출
filtered_image = np.zeros_like(image)
filtered_image[y:y+h, x:x+w] = image[y:y+h, x:x+w]  # 기존 이미지 => 배경 제거 이미지 덮어쓰기

cv2.namedWindow('delete background', cv2.WINDOW_NORMAL)
cv2.imshow('delete background', filtered_image)

cv2.imwrite('delete_background.jpg', filtered_image)


# ------ 경계선 for Text -------

filtered_bin = cv2.adaptiveThreshold(filtered_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 15)
filtered_bin_inv = 255 - filtered_bin

text_contours, _ = cv2.findContours(filtered_bin_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_image = np.zeros_like(filtered_image)
cv2.drawContours(contour_image, text_contours, -1, (255, 255, 255), 1)

cv2.namedWindow('text contour', cv2.WINDOW_NORMAL)
cv2.imshow('text contour', contour_image)

cv2.imwrite('text_contour.jpg', contour_image)


cv2.waitKey(0)
cv2.destroyAllWindows()