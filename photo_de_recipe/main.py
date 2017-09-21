#! -*- coding: utf-8 -*-

import numpy as np
import cv2

import object_detect as od
import inference as inf
import recipe

def main():
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
        frame, detect_img, detect_count = od.object_detect(frame)

        # 画面に表示
        cv2.imshow('Object Detection',frame)
        #print(detect_count)

        # キーボード入力待ち
        key = cv2.waitKey(1) & 0xFF

        # qが押された場合は終了
        if key == ord('q'):
            break

        # sが押された場合は保存
        if key == ord('s'):
            #print(inf.inference(frame))
            path = "/Users/kfukuda/Desktop/advse17/code/photo8.jpg"
            path2 = "/Users/kfukuda/Desktop/advse17/code/photo9.jpg"
            #cv2.imwrite(path,detect_img[0])
            #cv2.imwrite(path2,frame)
            result = inf.inference(path)
            print(result[0])
            # result2[0] = result[0]
            result2.append(result[0])
            print(result2)
            recipe.recipe(result2)



        # キャプチャの後始末と，ウィンドウをすべて消す
    cap.release()
    cv2.destroyAllWindows()


if __name__ ==  '__main__':
    main()
