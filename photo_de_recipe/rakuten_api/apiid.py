# -*- coding: utf-8 -*-
import requests,json
 #楽天APIカテゴリー一覧
url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426'
 
payload = {
    'applicationId': [1003080147854007200],
    'categoryType':'small',
   # 'elements':'ピーマン',
    }
 
r = requests.get(url, params=payload)
 
resp = r.json()
#print ("num of kensaku ="resp['count'])
print ('-'*40)
a = resp['result']
def apiid(int):
	#print(resp['result'])
	for i in a['small']:
		b = i['categoryName']
		if b == int:
			url = i['categoryUrl']
			id = url.split("/")    #urlの文字列を/で区切る
			print(id[4])           #4番目に検索に必要な情報がある
			return id[4]



#def hello(int):
#	b = int + 5
#	return b
