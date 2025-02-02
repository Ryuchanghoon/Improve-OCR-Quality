import cv2
import easyocr as ocr


img = cv2.imread('test.jpg')

reader = ocr.Reader(['ko', 'en'], gpu = False)

text = reader.readtext(img, detail = 0)

print(text)