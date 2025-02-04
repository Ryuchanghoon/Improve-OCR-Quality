import cv2
import numpy as np


image_path = "test.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# ------ Manual Thresholding -------

_, simple_binary = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)

combined_image = np.hstack((image, simple_binary))

cv2.namedWindow("Manual Thresholding", cv2.WINDOW_NORMAL)
cv2.imshow('Manual Thresholding', combined_image)

cv2.waitKey(0)
cv2.destroyAllWindows()