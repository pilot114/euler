from functools import reduce

numbers = [x for x in range(1, 101)]

one = reduce(lambda x, y: x+y, [i ** 2 for i in numbers])
two = reduce(lambda x, y: x+y, numbers) ** 2

print(two - one)
