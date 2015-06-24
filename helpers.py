# for check time execution (in Linux):
# time python yourprogram.py

def is_prime(n):
    if int(n) != n:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def next_prime():
	current = 2
	while True:
		if is_prime(current):
			yield current
		else:
			current+=1

# [1, 2, 3] => [1, 2, 3, 1*1, 2*2, 3*3, 1*2, 1*3, 2*3] => [1 ,2 ,3, 4, 6, 9]
# if deps = 2
# combo_bust([1 ,2 ,3, 4, 6, 9])
def combo_bust(input, deps = False):
	spongeInput = []
	for x in input:
		spongeInput.append(x)
		if not deps:
			yield x
	for x in input:
		for y in input:
			spongeInput.append(x*y)
			if not deps:
				yield x*y
	if deps:
		spongeInput = unique(spongeInput)
		yield from combo_bust(spongeInput, deps-1)

def unique(input):
    seen = set()
    seen_add = seen.add
    return [ x for x in input if not (x in seen or seen_add(x))]