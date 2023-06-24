# 密碼重試程式
# 先在程式中 設好密碼 password = 'a123456'
# 讓使用者最多輸入三次密碼
# 不對的話，就印出'密碼錯誤！還有_次機會'
# 對的話，就印出'登入成功'

# 較不好的版本(自己寫的)
# i = 2
# password = 'a123456'
# while i >= 0:
# 	pw = input('請輸入密碼: ')
# 	if pw != password:
# 		print('密碼錯誤！還有', i, '次機會')
# 		i = i - 1
# 		if i == -1:
# 			print('你已經沒機會囉')
# 	else:
# 		print('登入成功')
# 		break

# 老師版(會印出還有0次機會)
# password = 'a123456'
# i = 3 # 剩餘機會
# while i > 0:
# 	pwd = input('請輸入密碼: ')
# 	if pwd == password:
# 		print('登入成功')
# 		break
# 	else:
# 		i = i - 1
# 		print('密碼錯誤！還有', i, '次機會')
# 		if i == 0:
# 			print('你已經沒機會囉')
			# break # 如果用while True才需要印

# 完整版(不要印出還有0次機會)
password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤')
		if i > 0:
			print('密碼錯誤！還有', i, '次機會')
		else:
			print('沒機會嘗試了！要鎖帳號了')

# 額外練習版
# password = 'a123456'
# i = 3 # 剩餘機會
# while i > 0:
# 	i = i - 1
# 	pwd = input('請輸入密碼: ')
# 	if pwd == password:
# 		print('登入成功，你總共嘗試了', 3-i, '次')
# 		break
# 	else:
# 		print('密碼錯誤')
# 		if i > 0:
# 			print('密碼錯誤！還有', i, '次機會')
# 		else:
# 			print('沒機會嘗試了！要鎖帳號了')

