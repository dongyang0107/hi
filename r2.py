def read_file(filename):
	lines = []
	# encoding = 'utf-8-sig'：去掉讀取結果一開始的\ufeff
	with open (filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			# 把line一個個裝進去
			lines.append(line.strip())
	return lines

# 清單的分割
# n[開始值:結束值]：開始有包含，結束不包含
# n[:3]：可以拿前三個(開始值為0可不寫)
# n[-2:]：可以拿最後兩個(結尾值不寫表示到底)

def convert(lines):
	# person一開始沒有(還不知道說話的人是誰)
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	# split切割完會變清單，但無法知道每行被切成幾塊
	for line in lines:
		s = line.split(' ')
		# 將time和name取出來
		time = s[0]
		name = s[1]
		if name == 'Allen':
			# 貼圖記數
			if s[2] == '貼圖':
				allen_sticker_count = allen_sticker_count + 1
			elif s[2] == '圖片':
				allen_image_count = allen_image_count + 1
			else:
			# 文字記數
				for msg in s[2:]:
					allen_word_count = allen_word_count + len(msg)
		elif name == 'Viki':
			# 貼圖記數
			if s[2] == '貼圖':
				viki_sticker_count = viki_sticker_count + 1
			elif s[2] == '圖片':
				viki_image_count = viki_image_count + 1
			else:
			# 文字記數
				for msg in s[2:]:
					viki_word_count = viki_word_count + len(msg)
	print('allen說了', allen_word_count, '個字')
	print('allen傳了', allen_sticker_count, '個貼圖')
	print('allen傳了', allen_image_count, '張圖片')

	print('viki說了', viki_word_count, '個字')
	print('viki傳了', viki_sticker_count, '個貼圖')
	print('viki傳了', viki_image_count, '張圖片')


def write_file(filename, lines):
	with open (filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	# print(lines)
	lines = convert(lines)
	# write_file('output.txt', lines)

main()