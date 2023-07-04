# 檢查檔案在不在
import os # operating system

product = [] # 不管檔案存不存在都要執行此行(因為之後還有使用者輸入)
if os.path.isfile('products.csv'):
	print('yaeh! 找到檔案了')
	# 讀取檔案
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			# 把尾巴換行的符號去掉：strip()
			# 用逗點當作切割的標準：split(',')
			name, price = line.strip().split(',')
			# s = line.strip().split(',')
			# name = s[0]
			# price = s[1]
			# 若遇到'商品, 價格'不要顯示：continue
			if '商品, 價格' in line:
				continue #繼續(跳到下一回，不會跳出迴圈)
			p = [name, price]
			product.append(p)
	print(product)
else:
	print('找不到檔案......')

#讀取檔案
# product = []
# with open('products.csv', 'r', encoding = 'utf-8') as f:
# 	for line in f:
# 		# 把尾巴換行的符號去掉：strip()
# 		# 用逗點當作切割的標準：split(',')
# 		name, price = line.strip().split(',')
# 		# s = line.strip().split(',')
# 		# name = s[0]
# 		# price = s[1]
# 		# 若遇到'商品, 價格'不要顯示：continue
# 		if '商品, 價格' in line:
# 			continue #繼續(跳到下一回，不會跳出迴圈)
# 		p = [name, price]
# 		product.append(p)
# print(product)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = [name, price]
	product.append(p)
print(product)
print(product[0][0])
print(product[1][1])

# 印出所有購買紀錄
for p in product:
	print(p)
	print(p[0], '的價格', p[1])

# 寫入檔案
with open ('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品, 價格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')