with open ('3.txt', 'r', encoding = 'utf-8-sig') as f:
	lines = []
	for line in f:
		lines.append(line.strip())
# 時間和人名黏在一起，如何取出人名
# 字串可當作清單看待
for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print('時間: ', time)
	print('人名: ', name)


