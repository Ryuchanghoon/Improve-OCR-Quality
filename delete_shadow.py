import cv2
import numpy as np


image_path = "test.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#  가우시안 블러 적용 배경 추출
bg_blur = cv2.GaussianBlur(image, (55, 55), 0)
cv2.namedWindow('gaus blur', cv2.WINDOW_NORMAL)
cv2.imshow('gaus blur', bg_blur)

#  배경 제거 조명 보정
normalized = cv2.divide(image, bg_blur, scale = 255)
cv2.namedWindow('delete background', cv2.WINDOW_NORMAL)
cv2.imshow('delete background', normalized)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

top_hat = cv2.morphologyEx(normalized, cv2.MORPH_TOPHAT, kernel)
cv2.namedWindow('top_hat', cv2.WINDOW_NORMAL)
cv2.imshow('top_hat', top_hat)


bottom_hat = cv2.morphologyEx(normalized, cv2.MORPH_BLACKHAT, kernel)
cv2.namedWindow('bottom_hat', cv2.WINDOW_NORMAL)
cv2.imshow('bottom_hat', bottom_hat)



shadow_removed = cv2.add(normalized, top_hat)
shadow_removed = cv2.subtract(shadow_removed, bottom_hat)

cv2.namedWindow('shadow_removed', cv2.WINDOW_NORMAL)
cv2.imshow('shadow_removed', shadow_removed)


cv2.waitKey(0)
cv2.destroyAllWindows()