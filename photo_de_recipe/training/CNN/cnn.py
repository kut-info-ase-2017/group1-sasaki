#!/usr/local/bin/python
#! -*- coding: utf-8 -*-

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.models import load_model
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix
from PIL import Image
import cv2
import numpy as np
import sys

batch_size = 128
num_classes = 5
epochs = 12
img_rows, img_cols = 64, 64
dataset_size = 1602
teacher = []

# トマト読み込み
for i in range (dataset_size):
  src = cv2.imread('/Users/pinkmac/Desktop/sample/dataset/tomato/trans_images/resize/resize'+ str(i+1) +'.jpg')
  src = src.reshape(1,img_rows,img_cols,3)
  if i == 0:
    study = src
  else:
    study = np.append(study, src, axis=0)
  #配列に追加(教師データ)
  teacher.append('4')

#ブロッコリー読み込み
for i in range (dataset_size):
  src = cv2.imread('/Users/pinkmac/Desktop/sample/dataset/broccoli/trans_images/resize/resize'+ str(i+1) +'.jpg')
  src = src.reshape(1,img_rows,img_cols,3)
  study = np.append(study, src, axis=0)
  #配列に追加(教師データ)
  teacher.append('1')

#ナス読み込み
for i in range (dataset_size):
  src = cv2.imread('/Users/pinkmac/Desktop/sample/dataset/eggplant/trans_images/resize/resize'+ str(i+1) +'.jpg')
  src = src.reshape(1,img_rows,img_cols,3)
  study = np.append(study, src, axis=0)
  #配列に追加(教師データ)
  teacher.append('2')

#じゃがいも読み込み
for i in range (dataset_size):
  src = cv2.imread('/Users/pinkmac/Desktop/sample/dataset/potato/trans_images/resize/resize'+ str(i+1) +'.jpg')
  src = src.reshape(1,img_rows,img_cols,3)
  study = np.append(study, src, axis=0)
  #配列に追加(教師データ)
  teacher.append('3')

#にんじん読み込み
for i in range (dataset_size):
  src = cv2.imread('/Users/pinkmac/Desktop/sample/dataset/carrot/trans_images/resize/resize'+ str(i+1) +'.jpg')
  src = src.reshape(1,img_rows,img_cols,3)
  study = np.append(study, src, axis=0)
  #配列に追加(教師データ)
  teacher.append('0')

teacher=np.array(teacher)


x_train, x_test, y_train, y_test = cross_validation.train_test_split(study, teacher, test_size=0.3, random_state=0)


# input_shape = (img_rows, img_cols, 3)

# x_train = x_train.astype('float32')
# x_test = x_test.astype('float32')
# x_train /= 255
# x_test /= 255
# print('x_train shape:', x_train.shape)
# print(x_train.shape[0], 'train samples')
# print(x_test.shape[0], 'test samples')

# y_train = y_train.astype('int32')
# y_test = y_test.astype('int32')
# y_train = keras.utils.np_utils.to_categorical(y_train, num_classes)
# y_test =  keras.utils.np_utils.to_categorical(y_test, num_classes)

# model = Sequential()
# model.add(Conv2D(32, kernel_size=(3, 3),
#                  activation='relu',
#                  input_shape=input_shape))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(num_classes, activation='softmax'))

# model.compile(loss=keras.losses.categorical_crossentropy,
#               optimizer=keras.optimizers.Adadelta(),
#               metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs,
#           verbose=1, validation_data=(x_test, y_test))

# model.save('learning_cnn.h5')


model = load_model('learning_cnn_new.h5')
label_predict=model.predict_classes(x_test, batch_size=32, verbose=1)
label_predict=label_predict.astype(np.str)

print(confusion_matrix(y_test, label_predict))


