data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了，總共有', len(data), '筆資料')
print(data[0])

# 算留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
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

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])
print('------------------------')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言裡有good')
print(good[0])
print(good[1])

# 文字的計數
wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			# 去wc字典查找此word
			wc[word] = wc[word] + 1
		else:
			# 新增新的key進字典
			wc[word] = 1

for word in wc:
	# 若字出現超過100次
	if wc[word] > 100:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒有出現過喔')

print('感謝使用本查詢功能')


