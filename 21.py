def d(number):
	result = 0
	for x in range(1, number):
		if number%x == 0:
			result+=x
	return result

result = set()
for x in range(1, 10001):
	a = d(x)
	b = d(a)
	if x == b and a != b:
		result.add(a)
		result.add(b)
print(sum(result))
