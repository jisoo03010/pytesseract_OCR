import pytesseract 
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

a = Image.open('1.jpg')
# #사진속 글자를 텍스트로 변환해줌
d  = pytesseract.image_to_string(a, lang='kor')
print(d)