from functools import reduce

factorial = reduce(lambda x, y: x*y, [x for x in range(1, 101)])
print(reduce(lambda x, y: x+y, [int(x) for x in str(factorial)]))
