import cv2
import easyocr as ocr
from paddleocr import PaddleOCR


img = cv2.imread('improve_OCR_processor/test.jpg')

# ------ easyOCR -------

reader = ocr.Reader(['ko', 'en'], gpu = False)

text = reader.readtext(img, detail = 0)

print(text)


# ------ paddleOCR -------

paocr = PaddleOCR(lang = 'korean')

results = paocr.ocr(img, cls = True)

text_only = [line[1][0] for res in results for line in res]

print(text_only)