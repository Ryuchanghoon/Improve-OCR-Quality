import cv2
import numpy as np


image_path = "test.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


# ------ Normalization -------

bg_blur = cv2.GaussianBlur(image, (55, 55), 0)  # 가우시안 필터 55 by 55
normalized = cv2.divide(image, bg_blur, scale = 255)  # 범위 0~255 '정규화' 
cv2.namedWindow('Normalization', cv2.WINDOW_NORMAL)
cv2.imshow('Normalization', normalized)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))  # 모폴로지 연산(Top-hat, Bottom-hat) 사용 필터


# ------ 모폴로지 Top hat -------

top_hat = cv2.morphologyEx(normalized, cv2.MORPH_TOPHAT, kernel)
cv2.namedWindow('Top hat', cv2.WINDOW_NORMAL)
cv2.imshow('Top hat', top_hat)


# ------ 모폴로지 Bottom hat -------

bottom_hat = cv2.morphologyEx(normalized, cv2.MORPH_BLACKHAT, kernel)
cv2.namedWindow('Bottom hat', cv2.WINDOW_NORMAL)
cv2.imshow('Bottom hat', bottom_hat)


# ------ 그림자 제거 최종 연산 -------

shadow_removed = cv2.add(normalized, top_hat)
shadow_removed_final = cv2.subtract(shadow_removed, bottom_hat)
cv2.namedWindow('Final Shadow Removed', cv2.WINDOW_NORMAL)
cv2.imshow('Final Shadow Removed', shadow_removed_final)


cv2.waitKey(0)
cv2.destroyAllWindows()