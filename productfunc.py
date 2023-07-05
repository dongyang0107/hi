# 檢查檔案在不在
import os 

# 定義程式

# 讀取檔案
# products.csv改成filename，可每次讀不同檔案
def read_file(filename):
	product = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			name, price = line.strip().split(',')
			if '商品, 價格' in line:
				continue
			p = [name, price]
			product.append(p)
	return product

# 讓使用者輸入
def user_input(product):
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
	# product清單會有改變所以需要回傳結果
	return product

# 印出所有購買紀錄
def print_products(product):
	for p in product:
		print(p)
		print(p[0], '的價格', p[1])

# 寫入檔案
def write_file(filename, product):
	with open (filename, 'w', encoding = 'utf-8') as f:
		f.write('商品, 價格\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + '\n')


# 執行程式：def main()
# 檢查檔案在不在
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yaeh! 找到檔案了')
		product = read_file(filename)
	else:
		print('找不到檔案......')

	product = user_input(product)
	print_products(product)
	write_file('products.csv', product)

main()