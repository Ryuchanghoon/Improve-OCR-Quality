from flask import Flask, render_template, request, send_file, jsonify
import cv2
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

process_steps = []
current_image = None

@app.route('/')
def index():
    return render_template('index.html', process_steps='+'.join(process_steps))

@app.route('/upload', methods=['POST'])
def upload():
    global current_image, process_steps
    process_steps = []
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    current_image = filepath
    return jsonify({'message': 'File uploaded successfully', 'process_steps': '+'.join(process_steps)})

@app.route('/process/<action>', methods=['POST'])
def process(action):
    global current_image, process_steps
    if not current_image:
        return "No image uploaded", 400
    
    process_steps.append(action)
    current_image = apply_processing(current_image, action)
    return jsonify({'message': f'{action} applied', 'process_steps': '+'.join(process_steps)})

@app.route('/save', methods=['POST'])
def save():
    if not current_image:
        return "No processed image to save", 400
    
    processed_path = os.path.join(PROCESSED_FOLDER, os.path.basename(current_image))
    cv2.imwrite(processed_path, cv2.imread(current_image))
    return send_file(processed_path, as_attachment=True)

def apply_processing(image_path, action):
    image = cv2.imread(image_path)
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
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        mean_bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 15)
        mean_bin_inv = 255 - mean_bin
        contours, _ = cv2.findContours(mean_bin_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        filtered_image = np.zeros_like(image)
        filtered_image[y:y+h, x:x+w] = image[y:y+h, x:x+w]
        image = filtered_image
    processed_path = os.path.join(PROCESSED_FOLDER, os.path.basename(image_path))
    cv2.imwrite(processed_path, image)
    return processed_path

if __name__ == '__main__':
    app.run(debug=True)