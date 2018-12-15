import os
from flask import Flask, render_template, request
import cv2
import numpy as np
from keras.models import load_model
import tensorflow as tf

newmodel = load_model("E:\Inception\AutomateThePnumoniaDetection\Modifiedmodel.h5")

graph = tf.get_default_graph()

def ClsImg():
    global graph
    with graph.as_default():
        resize_dim = 256
        img = cv2.imread('E:\\Inception\\AutomateThePnumoniaDetection\\images\\01.png')
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

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        destination = "/".join([target, '01.png'])
        print(destination)
        file.save(destination)
    
    p = ClsImg()
    if p==1:
        return render_template("complete.html")
    else:
        return render_template("complete1.html")


if __name__ == "__main__":
    app.run(port=4555, debug=True)