def read_file(filename):
	lines = []
	# encoding = 'utf-8-sig'：去掉讀取結果一開始的\ufeff
	with open (filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			# 把line一個個裝進去
			lines.append(line.strip())
	return lines


def convert(lines):
	new = []
	# person一開始沒有(還不知道說話的人是誰)
	person = None
	# 把lines得東西一個個叫出來(一行行讀取)
	for line in lines:
		if line == 'Allen':
			# 代表現在說話的人是Allen
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		# 若person有值才做這行
		if person:
			# '+' 為字串的合併
			new.append(person + ': ' + line)
	return new


def write_file(filename, lines):
	with open (filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	# print(lines)
	lines = convert(lines)
	write_file('output.txt', lines)

main()