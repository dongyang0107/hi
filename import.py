# import載入(使用別人寫好的功能)
# random 隨機
# 套件(package)裝了很多的模組(module)
# import random
# randint：random integer
# r = random.randint(1, 100)
# print(r)

# 產生一個隨機整數1-100
# 讓使用者重複輸入數字去猜
# 猜對的話 印出'終於猜對了!'
# 猜錯的話 要告訴他 比答案大/小

# import random
# r = random.randint(1, 100)
# while True:
# 	num = input('請輸入數字吧: ')
# 	num = int(num)
# 	if r > num:
# 		print('比答案小，再猜一次')
# 	elif r < num:
# 		print('比答案大，再猜一次')
# 	else:
# 		print('終於猜對了')
# 		break

# 印出猜了幾次
# import random
# r = random.randint(1, 100)
# i = 0
# while True:
# 	num = input('請輸入數字吧: ')
# 	num = int(num)
# 	if r > num:
# 		print('比答案小，再猜一次')
# 		i = i + 1
# 	elif r < num:
# 		print('比答案大，再猜一次')
# 		i = i + 1
# 	else:
# 		i = i + 1
# 		print('終於猜對了, 你總共猜了', i, '次')
# 		break

# 印出猜了幾次(老師版)
# import random
# r = random.randint(1, 100)
# i = 0
# while True:
# 	i = i + 1
# 	num = input('請輸入數字吧: ')
# 	num = int(num)
# 	if r > num:
# 		print('比答案小，再猜一次')
# 	elif r < num:
# 		print('比答案大，再猜一次')
# 	else:
# 		print('終於猜對了')
# 		print('這是你猜的第', i, '次')
# 		break
# 	print('這是你猜的第', i, '次')

# 讓使用者決定隨機範圍
import random
start = input('請輸入隨機數字範圍開始值: ')
end = input('請輸入隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
i = 0
while True:
	i = i + 1
	num = input('請輸入數字吧: ')
	num = int(num)
	if r > num:
		print('比答案小，再猜一次')
	elif r < num:
		print('比答案大，再猜一次')
	else:
		print('終於猜對了')
		print('這是你猜的第', i, '次')
		break
	print('這是你猜的第', i, '次')
