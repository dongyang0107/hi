# 通常不知道輸入幾次用while-loop
# 用清單儲存輸入過的商品
# product = []
# while True:
# 	name = input('請輸入商品名稱: ')
# 	if name == 'q':
# 		break
# 	product.append(name)
# print(product)

# 若也要輸入名稱和價格===二維清單(清單中還有清單)
product = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = [name, price]
	# p = []
	# p.append(name)
	# p.append(price)
	# 之後再把小清單裝進大清單
	product.append(p)
print(product)
# 存取二維清單
print(product[0][0])
print(product[1][1])

# for-loop
for p in product:
	print(p)
	print(p[0], '的價格', p[1])

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# 寫入檔案(若沒有原檔也沒關係，電腦會自動生成新檔)
# txt產生文字檔，csv產生excel(可自己生成)
# 解決亂碼問題：encoding = 'utf-8'
with open ('products.csv', 'w', encoding = 'utf-8') as f:
	# 欄位名稱
	f.write('商品, 價格\n')
	for p in product:
		# 用加法做字串合併
		# 用逗點做區隔(若用excel就不會擠在同一格)
		# 真正的寫入
		f.write(p[0] + ',' + p[1] + '\n')