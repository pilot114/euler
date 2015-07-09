from itertools import permutations

i = 0
for x in permutations("0123456789"):
	i+=1
	if(i == 1000000):
		print("".join(x))
