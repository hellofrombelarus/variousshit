def randomhexcode(*args):
	import random
	qwerty=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
	while True:
		print(random.choice(qwerty), end='')
