# if a+b+c=1000 then max is 997
quadro = [x*x for x in range(1, 998)]

def find():
	for a2 in quadro:
		for b2 in quadro:
			c2 = a2+b2
			if c2 in quadro and a2**0.5+b2**0.5+c2**0.5 == 1000:
				return int(a2**0.5 * b2**0.5 * c2**0.5)
print(find())