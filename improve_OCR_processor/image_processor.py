import cv2
import numpy as np
import os
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage


class ImageProcessorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.current_image_path = None
        self.original_image = None 
        self.processed_image = None
        self.applied_filters = []

    def initUI(self):
        self.setWindowTitle('Image Processor')
        self.setGeometry(100, 100, 800, 700)

        self.label = QLabel(self)
        self.label.setText('No image loaded')

        self.filter_label = QLabel(self)
        self.filter_label.setText("Selected Filters: None")

        self.btn_upload = QPushButton('Upload Image', self)
        self.btn_upload.clicked.connect(self.upload_image)

        self.btn_normalize = QPushButton('Normalize', self)
        self.btn_normalize.clicked.connect(lambda: self.add_filter('normalize'))

        self.btn_remove_shadow = QPushButton('Remove Shadow', self)
        self.btn_remove_shadow.clicked.connect(lambda: self.add_filter('remove_shadow'))

        self.btn_convert_bw = QPushButton('Convert to B/W', self)
        self.btn_convert_bw.clicked.connect(lambda: self.add_filter('convert_bw'))

        self.btn_remove_bg = QPushButton('Remove Background', self)
        self.btn_remove_bg.clicked.connect(lambda: self.add_filter('remove_background'))

        self.btn_clahe = QPushButton('CLAHE', self)
        self.btn_clahe.clicked.connect(lambda: self.add_filter('clahe'))

        self.btn_prewitt = QPushButton('Apply Prewitt', self)
        self.btn_prewitt.clicked.connect(lambda: self.add_filter('prewitt'))

        self.btn_sobel = QPushButton('Apply Sobel', self)
        self.btn_sobel.clicked.connect(lambda: self.add_filter('sobel'))

        self.btn_contour = QPushButton('Contour', self)
        self.btn_contour.clicked.connect(lambda: self.add_filter('Contour'))

        self.btn_apply = QPushButton('Apply Filters', self)
        self.btn_apply.clicked.connect(self.apply_filters)

        self.btn_save = QPushButton('Save Image', self)
        self.btn_save.clicked.connect(self.save_image)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.filter_label)
        layout.addWidget(self.btn_upload)
        layout.addWidget(self.btn_normalize)
        layout.addWidget(self.btn_remove_shadow)
        layout.addWidget(self.btn_convert_bw)
        layout.addWidget(self.btn_remove_bg)
        layout.addWidget(self.btn_clahe)
        layout.addWidget(self.btn_prewitt)
        layout.addWidget(self.btn_sobel)
        layout.addWidget(self.btn_contour)
        layout.addWidget(self.btn_apply)
        layout.addWidget(self.btn_save)

        self.setLayout(layout)

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.jpg *.jpeg *.bmp)')
        if file_name:
            self.current_image_path = os.path.abspath(file_name)
            self.original_image = cv2.imdecode(np.fromfile(self.current_image_path, dtype=np.uint8), cv2.IMREAD_COLOR)

            if self.original_image is None:
                print(f"Error: Unable to load image from {self.current_image_path}")
                return

            self.applied_filters = []
            self.processed_image = self.original_image.copy()
            self.display_image(self.original_image)
            self.update_filter_label()

    def display_image(self, image):
        h, w = image.shape[:2]
        if len(image.shape) == 2:
            ch = 1
            bytes_per_line = w
            q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        else:
            ch = 3
            bytes_per_line = ch * w
            q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        pixmap = QPixmap.fromImage(q_image)
        self.label.setPixmap(pixmap.scaled(600, 400))

    def add_filter(self, action):
        self.applied_filters.append(action)
        self.update_filter_label()

    def update_filter_label(self):
        if self.applied_filters:
            self.filter_label.setText("Selected Filters: " + " + ".join(self.applied_filters))
        else:
            self.filter_label.setText("Selected Filters: None")

    def apply_filters(self):
        if self.original_image is None:
            print("Error: No image loaded")
            return

        image = self.original_image.copy()

        for action in self.applied_filters:
            if action != 'convert_bw' and len(image.shape) == 2:
                image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

            if action == 'normalize':
                bg_blur = cv2.GaussianBlur(image, (55, 55), 0)
                image = cv2.divide(image, bg_blur, scale=255)

            elif action == 'remove_shadow':
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
                top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
                bottom_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
                shadow_removed = cv2.add(image, top_hat)
                image = cv2.subtract(shadow_removed, bottom_hat)

            elif action == 'convert_bw':
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 15)

            elif action == 'remove_background':
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
                    image = filtered_image

            elif action == 'clahe':
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                clahe = cv2.createCLAHE(clipLimit = 5.0, tileGridSize = (3, 3))
                image = clahe.apply(gray)

            elif action == 'prewitt':
                image = image.astype(np.float32)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
                prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
                prewitt_edges_x = cv2.filter2D(gray, -1, prewitt_x)
                prewitt_edges_y = cv2.filter2D(gray, -1, prewitt_y)
                prewitt_edges = cv2.magnitude(prewitt_edges_x, prewitt_edges_y)
                image = cv2.normalize(prewitt_edges, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

            elif action == 'sobel':
                image = image.astype(np.float32)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
                sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)
                sobel_edges_x = cv2.filter2D(gray, -1, sobel_x)
                sobel_edges_y = cv2.filter2D(gray, -1, sobel_y)
                sobel_edges = cv2.magnitude(sobel_edges_x, sobel_edges_y)
                image = cv2.normalize(sobel_edges, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

            
            elif action == 'Contour':
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                mean_bin = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 15)
                mean_bin_inv = 255 - mean_bin

                text_contours, _ = cv2.findContours(mean_bin_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                filtered_image = np.zeros_like(image)
                cv2.drawContours(filtered_image, text_contours, -1, (255, 255, 255), 1)

                image = filtered_image




        self.processed_image = image
        self.display_image(image)

    def save_image(self):
        if self.processed_image is None:
            print("Error: No processed image to save")
            return
        save_path, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', 'Images (*.png *.jpg *.jpeg *.bmp)')
        if save_path:
            cv2.imencode('.jpg', self.processed_image)[1].tofile(save_path)


if __name__ == '__main__':
    app = QApplication([])
    window = ImageProcessorApp()
    window.show()
    app.exec_()