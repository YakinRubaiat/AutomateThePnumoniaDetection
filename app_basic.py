import os
from uuid import uuid4
from flask import Flask, render_template, request,send_from_directory
import cv2
import numpy as np

def ClsImg(filename):
    pass
     
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    # Image folder 
    target = os.path.join(APP_ROOT, 'images/')
    # target = os.path.join(APP_ROOT, 'static/')

    print(target)

    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))

    print(request.files.getlist("file"))

    for upload in request.files.getlist("file"):

        destination = "/".join([target, 'X_ray.png'])
        
        upload.save(destination)
    # return send_from_directory("images", filename, as_attachment=True)

    #return render_template("complete.html", image_name=filename,prob=100*p[0][0])

    return render_template("upload.html")

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5006)