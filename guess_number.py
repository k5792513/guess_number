import random
r = random.randint(1, 100)
while True:
	g = input('請猜猜看： ')
	g = int(g)
	if g == r:
		print('恭喜你終於猜對了！')
		break
	elif g > r:
		print('比答案大')
	else:
		print('比答案小')
