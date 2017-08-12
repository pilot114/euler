# WRONG
# from decimal import *

# periods = []
# for d in range(1,1000):
# 	getcontext().prec = 10000
# 	res = Decimal(1) / Decimal(d)
# 	decimal = str(res)[2:]

# 	checkpoints = []
# 	for x in range(1, int(len(decimal)/2)):
# 		turtle = decimal[x]
# 		rabbit = decimal[x+x]
# 		if turtle == rabbit:
# 			checkpoints.append(x)
# 	if len(checkpoints) > 4:
# 		periodFirst = checkpoints[2] - checkpoints[1]
# 		periodSecond = checkpoints[3] - checkpoints[2]
# 		periodThird = checkpoints[4] - checkpoints[3]
# 		if periodFirst == periodSecond and periodSecond == periodThird:
# 			periods.append(periodFirst)
# 		if periodFirst == 58:
# 			print(d)
# 			print(checkpoints)
# 			print(periodFirst)

# print(periods)
# print(max(periods))


# TRUE
def cycle_length(den):
    reste = 10
    i = 0
    while reste != 10 or i < 1:
        reste = (reste % den) * 10
        i += 1
    return i
longest = 0
for i in range(2, 1000):
    if i%2 != 0 and i%5 != 0:
        length = cycle_length(i)
        if length > longest:
            longest = length
            resultat = i
print(resultat)