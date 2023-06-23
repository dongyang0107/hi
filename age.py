# rain = input('請問今天有沒有下雨: ')
# == 檢查左右一不一樣
# if rain == '有':
	# print('撐傘出門')
	# print('買一包洋芋片')
	# print('在家看電影')
	# print('請在家看電影，別出門了吧')

# input存的內容為字串，而字串不能比較，所以需用int轉換成整數
# age = input('請輸入年齡: ')
# age = int(age)
# if age < 13:
# 	print('國小')
# elif age >= 13 and age < 18:
# 	print('國高中')
# elif age >= 18 and age < 22:
# 	print('大學')
# else:
# 	print('社會')

driving = input('請問你有沒有開過車？ ')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = input('請問你的年齡？ ')
age = int(age)

if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪 你怎麼會有開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照阿，怎麼還不去考')
	else:
		print('很好 再過幾年你就可以去考駕照了')
# else:
# 	print('只能輸入有或沒有喔')