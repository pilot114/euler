n = 2000000
a = [True] * n
for i in range(2, int(n**0.5)):
	for j in range(i * 2, n, i):
		a[j] = False
b = [i for i in range(2, n) if a[i]]
print(sum(b))
