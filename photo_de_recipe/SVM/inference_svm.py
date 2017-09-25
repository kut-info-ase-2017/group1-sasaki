#! -*- coding: utf-8 -*-

import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix
from PIL import Image
from skimage.feature import hog
import pickle
import os

def inference (img):
    converter = cv2.HOGDescriptor()

    # 学習モデルの読み込み
    loaded_model = pickle.load(open('learnig_model.sav', 'rb'))

    #判定したいしたいものを読み込む
    #src = img
    src = Image.open(img)
    resize = src.resize((200,150))
    src2 = np.asarray(resize)
    #src2 = img
    #src2 = cv.reshape(src2, src2, cv::Size(), 150.0/img.cols ,200.0/img.rows)
    #orgHeight, orgWidth = img.shape[:2]
    #size = (round(orgHeight/2), round(orgWidth/2))
    #src2 = cv2.resize(src2, (150,200))
    hog = converter.compute(src2)
    #1次元にしてる?
    hog2 = np.ravel(hog)

    result = loaded_model.predict(hog2)

    return result