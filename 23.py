def is_abundant(number):
	result = 1
	for x in range(2, int(number**0.5 + 1)):
		if number%x == 0:
			result+=x
			if x != number//x:
				result += number//x
	return result > number

limit = 28123

abundant = set()
for x in range(1,limit):
	if is_abundant(x):
		abundant.add(x)

all_sums = set()
for x in abundant:
	for y in abundant:
		if x+y <= limit:
			all_sums.add(x+y)

result = 0
for x in range(1,limit):
	if x not in all_sums:
		result+=x
print(result)
