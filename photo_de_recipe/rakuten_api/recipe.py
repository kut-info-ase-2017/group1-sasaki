# -*- coding: utf-8 -*-

import requests,json
from rakuten_api import apiid as my # apiidファイルから参照
import time
# import dht12 as temp
# import sys

# reload(sys) # sysモジュールをリロード
# sys.setdefaultencoding("utf-8") # デフォルトの文字コードを変更

# import api

# 楽天APIカテゴリー別ランキング
url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426'

def get_recipe(result, temp):
    #name = ['2'] #食材情報
    name = result
    # c = 26 #温度情報
    c = temp
    namelen = len(name)
    lenname = len(name)

    for q in range(0, lenname):
        if name[q] == 0:
            name[q] = 'にんじん'
        elif name[q] == 1:
            name[q] = 'ブロッコリー'
        elif name[q] == 2:
            name[q] = 'なす'
        elif name[q] == 3:
            name[q] = 'じゃがいも'
        elif name[q] == 4:
            name[q] = 'トマト'

    # 検出食材の表示
    for i in range(lenname):
        print('food%d: %s' % (i, name[i]))

    print('\n')

    # 季節を表すキーワード
    summer = ['夏','暑','つめたい','冷たい','そうめん','さっぱり','涼','ひんやり','さわやか','爽やか','なつ','熱中症','汗','素麺']
    winter = ['冬','熱々','アツアツ','ふゆ','鍋','寒','温ま','あたたまる','あつあつ','あったか','ぽかぽか','ポカポカ','ぽっかぽか','ホクホク','クリスマス']

    slen = len(summer)
    wlen = len(winter)
    season1 = [[0 for g in range(4)] for h in range(6)]
    season2 = [[0 for g in range(4)] for h in range(6)]
    count1 = [0]*5
    count2 = [0]*5
    for j in range(0,namelen):
        payload = {
            'applicationId': [1003080147854007200],
            'categoryId':my.apiid(name[j]), # apiidから食材情報を取得
            #'elements':'recipeTitle',
            }

        r = requests.get(url, params=payload)
        resp = r.json()
        print ('-'*40)
        print(name[j] + '料理\n')

        for i in resp['result']:
            print(i['recipeTitle'])
            print(i['recipeUrl'] + '\n')
            rd = i['recipeDescription']
            rt = i['recipeTitle']
            if c >= 25: # 高知の6月から8月の平均気温
                for p in range(0,slen):
                    ans1 = summer[p] in rd # ansにはpsの中に同じワードが入っていればTrueが入る
                    ans2 = summer[p] in rt

                    if ans1 == True:
                        season1[j][count1[j]] = rt
                        count1[j] = count1[j] + 1
                        break
                    elif ans2 == True:
                        season1[j][count1[j]] = rt
                        count1[j] = count1[j] + 1
                        break
            elif c <= 10: # 高知の12月から2月の平均気温
                for p in range(0,wlen):
                    ans1 = winter[p] in rd # ansにはpsの中に同じワードが入っていればTrueが入る
                    ans2 = winter[p] in rt

                    if ans1 == True:
                        season2[j][count2[j]] = rt
                        count2[j] = count2[j] + 1
                        break
                    elif ans2 == True:
                        season2[j][count2[j]] = rt
                        count2[j] = count2[j] + 1
                        break
        print()
        time.sleep(1)

    # レシピ名とurlの表示
    for k in range(0,namelen):
        if c >= 25 and count1[k] >= 1:
            print ('-'*40)
            print('夏のおすすめ ' + name[k] + '料理\n')
            for y in range(0,count1[k]):
                print(season1[k][y])
                print(i['recipeUrl'] + '\n')
            print()
        # elif c >= 25 and count1[k] == 0:
        #     print ('-'*40)
        #     print(name[k] + '夏のおすすめはありません')
        elif c <= 10 and count2[k] >= 1:
            print ('-'*40)
            print('冬のおすすめ ' + name[k] + '料理\n')
            for y in range(0,count2[k]):
                print(season2[y])
                print(i['recipeUrl'] + '\n')
            print()
        # elif c <= 10 and count1[k] == 0:
        #     print ('-'*40)
        #     print(name[k] + '冬のおすすめありません')
        #     print('\n')
