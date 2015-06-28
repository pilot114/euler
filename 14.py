def step(n):
	if  n%2 == 0:
		return n//2
	return 3*n+1

def find_max_chain(n):
	# number and chain_len
	result = [1, 1]
	for x in range(1,n):
		if x%2 == 0:
			continue
		chain_len = 1
		cur = x
		while cur != 1:
			cur = step(cur)
			chain_len+=1
		if chain_len > result[1]:
			result = [x, chain_len]
	return result[0]

print(find_max_chain(1000000))