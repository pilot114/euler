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