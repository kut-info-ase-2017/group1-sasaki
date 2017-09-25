#!/usr/local/bin/python
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


study=[]
teacher=[]
converter = cv2.HOGDescriptor()

# トマト読み込み
for i in range (360):
	src = cv2.imread('/Users/pinkmac/Desktop/sample/dataset/tomato/trans_images/resize/resize'+ str(i+1) +'.jpg')
	src2 = np.asarray(src)
	hog = converter.compute(src2)
	#1次元にしてる?
	hog2 = np.ravel(hog)
	#配列に追加(学習データ)
	study.append(np.asarray(hog2))
	#配列に追加(教師データ)
	teacher.append('tomato')

#ブロッコリー読み込み
for i in range (360):
	src = cv2.imread('/Users/pinkmac/Desktop/sample/dataset/broccoli/trans_images/resize/resize'+ str(i+1) +'.jpg')
	src2 = np.asarray(src)
	hog = converter.compute(src2)
	#1次元にしてる?
	hog2 = np.ravel(hog)
	#配列に追加(学習データ)
	study.append(np.asarray(hog2))
	#配列に追加(教師データ)
	teacher.append('broccoli')

#ナス読み込み
for i in range (360):
	src = cv2.imread('/Users/pinkmac/Desktop/sample/dataset/eggplant/trans_images/resize/resize'+ str(i+1) +'.jpg')
	src2 = np.asarray(src)
	hog = converter.compute(src2)
	#1次元にしてる?
	hog2 = np.ravel(hog)
	#配列に追加(学習データ)
	study.append(np.asarray(hog2))
	#配列に追加(教師データ)
	teacher.append('eggplant')

#にんじん読み込み
for i in range (360):
	src = cv2.imread('/Users/pinkmac/Desktop/sample/dataset/carrot/trans_images/resize/resize'+ str(i+1) +'.jpg')
	src2 = np.asarray(src)
	hog = converter.compute(src2)
	#1次元にしてる?
	hog2 = np.ravel(hog)
	#配列に追加(学習データ)
	study.append(np.asarray(hog2))
	#配列に追加(教師データ)
	teacher.append('carrot')

#じゃがいも読み込み
for i in range (360):
	src = cv2.imread('/Users/pinkmac/Desktop/sample/dataset/potato/trans_images/resize/resize'+ str(i+1) +'.jpg')
	src2 = np.asarray(src)
	hog = converter.compute(src2)
	#1次元にしてる?
	hog2 = np.ravel(hog)
	#配列に追加(学習データ)
	study.append(np.asarray(hog2))
	#配列に追加(教師データ)
	teacher.append('potato')

study2=np.array(study)
teacher2=np.array(teacher)


tuned_parameters = [
    {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
    # {'C': [1], 'kernel': ['rbf'], 'gamma': [1]},
    # {'C': [1, 10, 100, 1000], 'kernel': ['rbf'], 'gamma': [1, 0.1, 0.01, 0.00001]},
    #{'C': [1, 10, 100, 1000], 'kernel': ['poly'], 'degree': [2, 3, 4], 'gamma': [0.00001, 0.000001, 0.0000001]},
    #{'C': [1, 10, 100, 1000], 'kernel': ['sigmoid'], 'gamma': [0.001, 0.0001]}
    ]


X_train, X_test, y_train, y_test = cross_validation.train_test_split(study2, teacher2, test_size=0.3, random_state=0)

score = 'f1'
clf = GridSearchCV(
    SVC(C=1), # 識別器
    tuned_parameters, # 最適化したいパラメータセット 
    cv=8, # 交差検定の回数
    scoring='%s_weighted' % score ) # モデルの評価関数の指定

clf.fit(X_train, y_train)
pickle.dump(clf, open('learnig_model.sav', 'wb'))

loaded_model = pickle.load(open('learnig_model.sav', 'rb'))
label_predict = loaded_model.predict(X_test)

print(confusion_matrix(y_test, label_predict))


# # 学習モデルの読み込み
# loaded_model = pickle.load(open('learnig_model.sav', 'rb'))

# #判定したいしたいものを読み込む
# src = Image.open('/Users/pinkmac/Desktop/sample/test.jpg')
# resize = src.resize((200,150))
# src2 = np.asarray(resize)
# hog = converter.compute(src2)
# #1次元にしてる?
# hog2 = np.ravel(hog)

# result=loaded_model.predict(hog2)
# print(result)
