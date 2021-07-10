import numpy
from flask import Flask, render_template, request
import cv2
from gtts import gTTS
import os
import pytesseract
from pytesseract import Output
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == 'POST':
        img = request.files['img'].read()
        npimg = numpy.fromstring(img, numpy.uint8)
        img1 = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        tt = pytesseract.image_to_string(img1)
        output = gTTS(text=tt, lang='en', slow=False)
        output.save("output.mp3")
        os.system("start output.mp3")
        return render_template('index.html', text1=tt)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
