def test():
	with open('grid.txt', 'rt', encoding='utf-8') as f:
		for line in f:
			pos = line.split(' ')
			x = int(pos[0])-1
			y = int(pos[1])-1
			z = int(pos[2], 2)
			print(x,' ',y,' ',z)