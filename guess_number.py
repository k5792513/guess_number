import random
start = input('請輸入開始值: ')
end = input('請輸入結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
x = 0
while True:
	x = x + 1
	g = input('請猜猜看： ')
	g = int(g)
	if g == r:
		print('恭喜你終於猜對了！')
		break
	elif g > r:
		print('比答案大')
	else:
		print('比答案小')
	print('猜了', x, '次')
print('猜了', x, '次')