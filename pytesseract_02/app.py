from cProfile import label
from flask import Flask, render_template, jsonify, request
import io
import json
import os
from numpy import reshape
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import torch.nn as nn
import requests
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import  utils
import torchvision.datasets as datasets
import splitfolders
import torch.nn.functional as F

# ocr 관련 모듈
import pytesseract 
from PIL import Image 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#모델 가져오기
# model.load_state_dict(torch.load('model.pt'))

# 이미지 나누기 
# splitfolders.ratio('./static/dataset2/', output="./static/sample_data/", seed=1337, ratio=(0.8, 0.2))

#모델 저장하기 
# model = torch.save(model.state_dict(), 'model.pt')
# print(model)

app = Flask(__name__)

# ====================================================
@app.route("/upload", methods=['POST'])
def upload():
    file_upload = request.files['file_lo'] # 받아온 파일 
    #predict함수 안에 매개변수로 받아온 파일을 넘겨준다.
    pp = predict(file_upload)
    print("  pp=========>",   pp)
    output_text =  {"1" : "{}".format(pp[0]), "2" : "{}".format(pp[1]),  "3" : "{}".format(pp[2])}
    print("output_text=====>", output_text)
    return jsonify(output_text)

def predict(input_img):
# 이미지 전처리하는 부분
    a = Image.open(input_img)
    # #사진속 글자를 텍스트로 변환해줌
    d  = pytesseract.image_to_string(a, lang='kor+eng')
    d = d.split('\n')
    return d
# 
#==서버===========================================================================


@app.route('/')
def hello():
   return "OCR test"



@app.route('/main', methods=['GET', 'POST'])
def main():
    value = 'fdsadfdsf, python'
    return render_template("main.html", value = value)

# 
if __name__ == "__main__":
    app.run()
