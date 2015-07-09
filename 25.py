def finnobachi():
	x = 1
	y = 2
	yield 1
	yield x
	yield y
	while True:
		x, y = y, x + y
		yield y

source = finnobachi()

# muhahhaha
for index in range(1,1000000000000000000000000000000000000000000):
	if len(str(source.__next__())) == 1000:
		print(index)
		break
