import cv2


image_path = "test.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

height, width = image.shape
print(f'height: {height}, width: {width}')  # 이미지 가로, 세로 크기

# 블록 크기에 따른 빨간 선
def draw_grid(image, block_size=51):
    grid_img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    for x in range(0, width, block_size):
        cv2.line(grid_img, (x, 0), (x, height), (0, 0, 255), 1)
    for y in range(0, height, block_size):
        cv2.line(grid_img, (0, y), (width, y), (0, 0, 255), 1)
    return grid_img

block_check = draw_grid(image)

cv2.namedWindow('block check', cv2.WINDOW_NORMAL)
cv2.imshow('block check', block_check)


# ------ Mean Adaptive Thresholding -------

mean_bin = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 15)

cv2.namedWindow('mean thresholding', cv2.WINDOW_NORMAL)
cv2.imshow('mean thresholding', mean_bin)


# ------ Gaussian Adaptive Thresholding -------

gaus_bin = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 15)

cv2.namedWindow('Gaus Thresholding', cv2.WINDOW_NORMAL)
cv2.imshow('Gaus Thresholding', gaus_bin)


cv2.waitKey(0)
cv2.destroyAllWindows()