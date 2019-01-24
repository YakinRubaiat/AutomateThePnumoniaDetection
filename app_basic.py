import os
from uuid import uuid4
from flask import Flask, render_template, request,send_from_directory
import cv2
import numpy as np
from keras.models import load_model
import tensorflow as tf

newmodel = load_model("E:\Inception\AutomateThePnumoniaDetection\ProbablityModel.h5")

graph = tf.get_default_graph()

def ClsImg(filename):
    global graph
    with graph.as_default():
        resize_dim = 224
        img = cv2.imread('E:\\Inception\\AutomateThePnumoniaDetection\\images\\'+filename)
        img=cv2.resize(img,(resize_dim,resize_dim),interpolation=cv2.INTER_AREA)
        img = np.array(img)
        img = img[np.newaxis,:,:,:]
        p = newmodel.predict(img)
        return p

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    p= ClsImg(filename)    

    print(p[0][0])

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete.html", image_name=filename,prob=100*p[0][0])

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5006)