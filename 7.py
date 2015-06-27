def is_prime(n):
    if int(n) != n:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def prime_gen():
	current = 2
	yield current
	while True:
		current+=1
		if is_prime(current):
			yield current

primes = []
source = prime_gen()
for x in range(1,10002):
	primes.append(source.__next__())
print(primes[10000])
