from cv2 import split
import pytesseract 
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

a = Image.open('Example_01.png')
# #사진속 글자를 텍스트로 변환해줌
d  = pytesseract.image_to_string(a, lang='kor+eng')
d = d.split('\n')

output_text =  {"1" : "%s"%d[0], "2" : "%s"%d[1],  "3" : "%s"%d[2]}
print(output_text)