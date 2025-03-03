import cv2
import numpy as np
import os
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import button_func


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
        
        self.btn_apply = QPushButton('Apply', self)
        self.btn_apply.clicked.connect(self.apply_filters)
        
        self.btn_refresh = QPushButton('Refresh', self)
        self.btn_refresh.clicked.connect(self.refresh_image)  # 새로고침

        self.buttons = {
            'Remove Shadow': 'remove_shadow',
            'GrayScale': 'grayscale',
            'Remove Background': 'remove_background',
            'CLAHE': 'clahe',
            'Apply Prewitt': 'prewitt',
            'Apply Sobel': 'sobel',
            'Contour': 'contour',
            'Mean Adaptive Threshold': 'mean_thresh',
            'Gaussian Adaptive Threshold': 'gauss_thresh',
            'Morphology Opening': 'morph_open',
            'Morphological Closing': 'morph_close',
            'Top Hat': 'top_hat',
            'Bottom Hat': 'bottom_hat'
        }
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.filter_label)
        layout.addWidget(self.btn_upload)
        
        self.button_widgets = []
        for text, action in self.buttons.items():
            btn = QPushButton(text, self)
            btn.clicked.connect(lambda checked, act=action: self.add_filter(act))
            layout.addWidget(btn)
            self.button_widgets.append(btn)
        
        layout.addWidget(self.btn_apply)
        layout.addWidget(self.btn_refresh)
        
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

    def refresh_image(self):
        if self.original_image is not None:
            self.processed_image = self.original_image.copy()
            self.applied_filters = []
            self.display_image(self.processed_image)
            self.update_filter_label()
        else:
            print("Error: No image loaded")

    def update_filter_label(self):
        if self.applied_filters:
            self.filter_label.setText("Selected: " + " + ".join(self.applied_filters))
        else:
            self.filter_label.setText("Selected: None")

    def apply_filters(self):
        if self.original_image is None:
            print("Error: No image loaded")
            return

        image = self.original_image.copy()

        for action in self.applied_filters:
            if hasattr(button_func, action):
                image = getattr(button_func, action)(image)
            else:
                print(f"Warning: Function {action} not found in button_func module")

        self.processed_image = image
        self.display_image(image)

if __name__ == '__main__':
    app = QApplication([])
    window = ImageProcessorApp()
    window.show()
    app.exec_()