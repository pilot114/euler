epicNumber = 600851475143
primes = []
for d in range(2,int(epicNumber**0.5)):
    while (epicNumber % d) == 0:
        primes.append(d)
        epicNumber //= d
if epicNumber > 1:
   primes.append(epicNumber)
print(max(primes))