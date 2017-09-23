# -*- coding: utf-8 -*-
import requests,json
import apiid as my    #apiidファイルから参照
import time
#import api
#楽天APIカテゴリー別ランキング

def recipe(name):

	url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426'

	#name = ['tomato','carrot','eggplant']	#食材情報
	c = 27							#温度情報
	namelen = len(name)

	lenname = len(name)
	for q in range(0,lenname):
		if name[q] == 'tomato':
			name[q] = 'トマト'
		elif name[q] == 'eggplant':
			name[q] = 'なす'
		elif name[q] == 'broccoli':
			name[q] = 'ブロッコリー'
		elif name[q] == 'carrot':
			name[q] = 'にんじん'
		elif name[q] == 'potato':
			name[q] = 'じゃがいも'		



	 


	summer = ['夏','寒','つめたい','冷']			#気温がたかいときに食べたいワード
	winter = ['冬','熱','あつい','暑','鍋']		#気温が低いときに食べたいワード


	slen = len(summer)
	wlen = len(winter)
	season1 = [0]*30
	season2 = [0]*30
	count1 = 0
	count2 = 0
	for j in range(0,namelen):

		payload = {
			'applicationId': [1003080147854007200],
			'categoryId':my.apiid(name[j]),	    #apiidから食材情報を取得
			#'elements':'recipeTitle',
			}

		r = requests.get(url, params=payload)
		resp = r.json()
		print ('-'*40)
		print(name[j] + '\n')

		for i in resp['result']:
			print(i['recipeTitle'])
			print(i['recipeUrl'])
			rd = i['recipeDescription']
			rt = i['recipeTitle']
			if c > 26:	
				for p in range(0,slen):
					ans1 = summer[p] in rd      #ansにはpsの中に同じワードが入っていればTrueが入る
					ans2 = summer[p] in rt

					if ans1 == True:
						season1[count1] = rt
						count1 = count1 + 1
						break
					elif ans2 == True:
						season1[count1] = rt
						count1 = count1 + 1
						break
			elif c < 20:
				for p in range(0,wlen):
					ans1 = winter[p] in rd      #ansにはpsの中に同じワードが入っていればTrueが入る
					ans2 = winter[p] in rt

					if ans1 == True:
						season2[count2] = rt
						count2 = count2 + 1
						break
					elif ans2 == True:
						season2[count2] = rt
						count2 = count2 + 1
						break
		time.sleep(1)

	if c > 26 and count1 >= 1:
		print ('-'*40)		
		print('夏に食べよう\n')	
		for y in range(0,count1):
			print(season1[y])
			print(i['recipeUrl'])
	elif c < 20 and count2 >= 1:	
		print ('-'*40)	
		print('冬に食べよう\n')	
		for y in range(0,count2):
			print(season2[y])
			print(i['recipeUrl'])
		