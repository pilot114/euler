# https://en.wikipedia.org/wiki/Least_common_multiple
from functools import reduce

dividers = [x for x in range(1, 21)]
primes = [2, 3, 5, 7, 11, 13, 17, 19]
result_primes = []
primeUpFlag = False
primeIndex = 0

while sum(dividers) != len(dividers):
	primeUpFlag = True
	for x in dividers:
		if x%primes[primeIndex] == 0:
			dividers[dividers.index(x)] = x//primes[primeIndex]
			primeUpFlag = False
	if primeUpFlag:
		primeIndex += 1
		primeUpFlag = False
	else:
		result_primes.append(primes[primeIndex])

print(reduce(lambda x, y: x*y, result_primes))
