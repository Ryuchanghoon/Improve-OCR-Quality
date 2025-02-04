import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = "test.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# ------ Manual Thresholding -------

_, simple_binary = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)

combined_image = np.hstack((image, simple_binary))

cv2.namedWindow("Manual Thresholding", cv2.WINDOW_NORMAL)
cv2.imshow('Manual Thresholding', combined_image)

# ------ Otsu's Thresholding -------

_, otsu_binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])


plt.plot(hist, color='black')
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()


cv2.namedWindow('Otsu thresholding', cv2.WINDOW_NORMAL)
cv2.imshow('Otsu thresholding', otsu_binary)

cv2.waitKey(0)
cv2.destroyAllWindows()