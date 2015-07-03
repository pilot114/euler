mapped = {
	1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
	11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8,
	20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6
}
summa = 0
for x in range(1,1000):
	if x >= 100:
		summa += mapped[x//100] + 7 # "hundred"
		x %= 100
		if x:
			summa += 3 # "and"
	if x in mapped:
		summa += mapped[x]
	elif x:
		summa += mapped[x-x%10] + mapped[x%10]
# for 1000
print(summa+11)
