#! -*- coding: utf-8 -*-

import cv2
import numpy as np

# 指定した画像(path)の物体を検出
def object_detect(path):

    # 検出画像の保存用
    detect = []

    # 画像の読み込み、出力画像用（検出領域の描写）
    #img = cv2.imread(path)
    #detect_all = cv2.imread(path)
    img, detect_all = path, path;

    # グレースケール画像へ変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # フィルタ処理
    filtered = cv2.GaussianBlur(gray, (11, 11), 0)

    # 2値化
    #   背景を落とす
    retval, thresh_back = cv2.threshold(filtered, 120, 255, cv2.THRESH_BINARY)
    #   境界の明確化
    retval, thresh_clarify = cv2.threshold(filtered, 200, 255, cv2.THRESH_BINARY_INV)
    thresh = np.minimum(thresh_back, thresh_clarify)

    # 輪郭を抽出
    #   contours : [領域][Point No][0][x=0, y=1]
    #   cv2.CHAIN_APPROX_NONE: 中間点も保持する
    #   cv2.CHAIN_APPROX_SIMPLE: 中間点は保持しない
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    # 矩形検出された数（デフォルトで0を指定）
    detect_count = 0

    # 各輪郭に対する処理
    for i in range(0, len(contours)):

      # 輪郭の領域を計算
      area = cv2.contourArea(contours[i])

      # ノイズ（小さすぎる領域）と全体の輪郭（大きすぎる領域）を除外
      if area < 1e3 or 1e5 < area:
        continue

      # 外接矩形
      if len(contours[i]) > 0:
        rect = contours[i]
        x, y, w, h = cv2.boundingRect(rect)
        cv2.rectangle(detect_all, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 外接矩形毎に画像を保存
        #cv2.imwrite('photo/detect' + str(detect_count) + '.jpg', img[y:y + h, x:x + w])
        detect.append(img[y:y + h, x:x + w])
        detect_count = detect_count + 1

    #cv2.imwrite('photo/detect_all.jpg', detect_all)
    #cv2.imshow('detect', detect_all)
    #cv2.waitKey(0)

    #return detect_count
    return detect_all, detect, detect_count
