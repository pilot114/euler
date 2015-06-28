size = 20
paths = 1

for x in range(0,size):
	paths *= (2*size)-x
	paths /= x+1
print(int(paths))