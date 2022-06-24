import keras
from keras.models import load_model
from scipy import misc, spatial
from PIL import Image
import numpy as np
import cv2


model = load_model("handwritten_digits.h5")

def predict(InputImg):

    image = cv2.imread(InputImg)[:, :, 0]


    #image = cv2.imread(InputImg)
    #image = np.invert(np.array([image]))
    # image = image[:, :, 0]

    image = np.invert(image)
    image = cv2.resize(image, (28, 28))
    image = image.reshape(1,28,28,1)

    #image = cv2.resize(image,None,fx = 28, fy = 28)

    return model.predict(image)[0].tolist().index(1)

