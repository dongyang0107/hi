# 讀取檔案
# r：read   w：write
# strip()：把換行符號、多於空格去掉(針對字串的功能，其他不行)
# 有with時，離開with的架構時檔案會自動close(line 8)
# data = []
# with open('food.txt', 'r') as f:
# 	for line in f:
# 		data.append(line.strip())

# print(data)

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count = count + 1
		# 每讀一千筆印一次，以便知道讀取進度
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了，總共有', len(data), '筆資料')

# 算留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
 	# print(sum_len)
print('留言的平均長度為', sum_len/len(data))

print('------------------------')
print(len(data[0]))
print(data[0])
print('------------------------')
print(data[1])
print('------------------------')
print(data[2])
print('------------------------')
# 第1000000筆資料
print(data[999999])

