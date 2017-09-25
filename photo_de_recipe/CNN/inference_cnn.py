#! -*- coding: utf-8 -*-

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.models import load_model
from sklearn import cross_validation
from PIL import Image
import cv2
import numpy as np
import sys
# from tensorflow.contrib.keras.python.keras import backend

# import warnings
# warnings.filterwarnings('ignore')

def inference_cnn(path):
    batch_size = 128
    num_classes = 5
    epochs = 12
    img_rows, img_cols = 64, 64
    dataset_size = 360
    teacher = []

    model = load_model('CNN/learning_cnn_64.h5')

    #src = Image.open('../photo/test.jpg')
    src = Image.open(path)
    src = src.resize((img_rows, img_cols))
    src2 = np.asarray(src)
    src2 = src2.reshape(1,img_rows,img_cols,3)

    predict = model.predict_classes(src2, batch_size=32, verbose=1)

    # print(predict)
    # backend.clear_session()

    return predict


#if __name__ == '__main__':
 #   inference_cnn('../photo/test.jpg')