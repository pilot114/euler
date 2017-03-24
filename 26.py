cicles = []
for d in range(1,1000):
	decimal = str(1/d)[2:]

	print(decimal)
	# race!
	checkpoints = []
	for x in range(, int(len(decimal)/2)):
		turtle = decimal[x]
		rabbit = decimal[x+x]
		if turtle == rabbit:
			checkpoints.append(x)
	if checkpoints:
		print(checkpoints)
