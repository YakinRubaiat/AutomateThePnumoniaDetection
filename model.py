from keras.models import load_model
import cv2
import numpy as np


newmodel = load_model("E:\Inception\AutomateThePnumoniaDetection\Modifiedmodel.h5")



resize_dim = 256
img = cv2.imread('E:\\Inception\\AutomateThePnumoniaDetection\\images\\01.png')
img=cv2.resize(img,(resize_dim,resize_dim),interpolation=cv2.INTER_AREA)
img = np.array(img)
img = img[np.newaxis,:,:,:]
p = newmodel.predict(img)
if p==1:
    print("Here")
else:
     print("wjbkvj")


