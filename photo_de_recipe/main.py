#! -*- coding: utf-8 -*-

import numpy as np
import cv2

import object_detect as od
import recv_temp
from CNN import inference_cnn
from rakuten_api import recipe

path = "photo/"
result = [] # 認識結果の保存


def cap():
    # webカメラを選択
    cap = cv2.VideoCapture(1)

    #カメラの解像度を設定
    #cap.set(3, 640)  # Width
    #cap.set(4, 480)  # Height
    #cap.set(5, 15)   # FPS

    cap.set(3, 1000)  # Width
    cap.set(4, 600)  # Height
    cap.set(5, 15)   # FPS

    result2 = []

    while(True):
        # フレームをキャプチャ
        ret, frame = cap.read()

        # 物体の検出結果を取得
        detect_all, detect, detect_count = od.object_detect(frame)

        # 画面に表示
        cv2.imshow('frame', detect_all)
        #cv2.imshow('Object Detection',frame)
        #print(detect_count)

        # キーボード入力待ち
        key = cv2.waitKey(1) & 0xFF

        # qが押された場合は終了
        if key == ord('q'):
            break

        # sが押された場合は保存
        if key == ord('s'):
            #cv2.imwrite(cap_path, frame)
            break
            #print(inf.inference(frame))
            #path = "/Users/kfukuda/Desktop/advse17/code/photo8.jpg"
            #path2 = "/Users/kfukuda/Desktop/advse17/code/photo9.jpg"
            #cv2.imwrite(path,detect_img[0])
            #cv2.imwrite(path2,frame)
            #result = inf.inference(path)
            #print(result[0])
            # result2[0] = result[0]
            #result2.append(result[0])
            #print(result2)
            #recipe.recipe(result2)

    # キャプチャの後始末と，ウィンドウをすべて消す
    cap.release()
    cv2.destroyAllWindows()

    return detect_all, detect, detect_count


def main():
    detect_all, detect, detect_count = cap() # 物体検出対象の画像を取得

    cv2.imshow('detect', detect_all) # 検出物体の表示
    cv2.waitKey(0)

    cv2.imwrite(path + 'detect_all.jpg', detect_all) # 検出物体の保存
    for i in range(detect_count): # 検出物体の切り出し、保存
        cv2.imwrite(path + 'detect' + str(i) + '.jpg', detect[i])


    for i in range(detect_count): # 物体の認識
        result_tmp = inference_cnn.inference_cnn(path + 'detect' + str(i) + '.jpg')
        print(result_tmp)
        if (result not in result_tmp): result.append(int(result_tmp))

    temp = recv_temp.temperture() # raspberry pi から温度情報を取得

    recipe.get_recipe(result, temp)


if __name__ ==  '__main__':
    main()
