#!/usr/local/bin/python
#! -*- coding: utf-8 -*-

import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from PIL import Image
from skimage.feature import hog
import pickle
import os


study=[]
teacher=[]
converter = cv2.HOGDescriptor()


filenames_tomato = os.listdir('./dataset/tomato/trans_images')
filenames_broccoli = os.listdir('./dataset/broccoli/trans_images')
filenames_eggplant = os.listdir('./dataset/eggplant/trans_images')
filenames_carrot = os.listdir('./dataset/carrot/trans_images')
filenames_potato = os.listdir('./dataset/potato/trans_images')


# #トマトリサイズ
# i=0
# for name in filenames_tomato:
# 	if name.endswith('.jpg'):
# 		img = Image.open('./dataset/tomato/trans_images/' + str(name))
# 		resize = img.resize((200,150))
# 		i = i + 1
# 		resize.save("/Users/pinkmac/Desktop/sample/dataset/tomato/trans_images/resize/resize"+ str(i) +".jpg")


# #ブロッコリーリサイズ
# i=0
# for name in filenames_broccoli:
# 	if name.endswith('.jpg'):
# 		img = Image.open('./dataset/broccoli/trans_images/' + str(name))
# 		resize = img.resize((200,150))
# 		i = i + 1
# 		resize.save("/Users/pinkmac/Desktop/sample/dataset/broccoli/trans_images/resize/resize"+ str(i) +".jpg")

# #ナスリサイズ
# i=0
# for name in filenames_eggplant:
# 	if name.endswith('.jpg'):
# 		img = Image.open('./dataset/eggplant/trans_images/' + str(name))
# 		resize = img.resize((200,150))
# 		i = i + 1
# 		resize.save("/Users/pinkmac/Desktop/sample/dataset/eggplant/trans_images/resize/resize"+ str(i) +".jpg")


#にんじんリサイズ
i=0
for name in filenames_carrot:
	if name.endswith('.jpg'):
		img = Image.open('./dataset/carrot/trans_images/' + str(name))
		resize = img.resize((200,150))
		i = i + 1
		resize.save("/Users/pinkmac/Desktop/sample/dataset/carrot/trans_images/resize/resize"+ str(i) +".jpg")


#じゃがいもリサイズ
i=0
for name in filenames_potato:
	if name.endswith('.jpg'):
		img = Image.open('./dataset/potato/trans_images/' + str(name))
		resize = img.resize((200,150))
		i = i + 1
		resize.save("/Users/pinkmac/Desktop/sample/dataset/potato/trans_images/resize/resize"+ str(i) +".jpg")








