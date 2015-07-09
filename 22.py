text = open("resources/p022_names.txt").readline()
names = [s[1:-1] for s in text.split(',')]

# ord('A') - ASCII_shift = 1
ASCII_shift = 64

i = 0
result = 0
for name in sorted(names):
	i+=1
	result += i * sum([ord(letter)-ASCII_shift for letter in name])
print(result)
