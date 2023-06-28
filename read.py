# 讀取檔案
# r：read   w：write
# strip()：把換行符號、多於空格去掉(針對字串的功能，其他不行)
# 有with時，離開with的架構時檔案會自動close(line 8)
# data = []
# with open('food.txt', 'r') as f:
# 	for line in f:
# 		data.append(line.strip())

# print(data)
# print(len(data))
# print(data[0])
# print(len(data[0]))

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
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
print(len(data[1]))
print(data[1])
print('------------------------')
print(data[2])
print('------------------------')
# 第1000000筆資料
print(data[999999])
print('------------------------')

# 清單篩選
# 有多少留言長度小於100字
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])
print('------------------------')

# 有提到good的篩選出來
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言裡有good')
print(good[0])
print(good[1])

# 有提到good的篩選出來(更快速的寫法)
good = [d for d in data if 'good' in d]
# 用'bad' in d，每一筆問有沒有bad，如果有就印true，沒有就印false，所以會有1000000筆的true和false
bad = ['bad' in d for d in data]

bad = []
for d in data:
	bad.append('bad' in d)