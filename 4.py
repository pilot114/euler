
max = 0
for x in reversed(range(100,999)):
    for y in reversed(range(100,999)):
        z = x*y
        if(str(z) == str(z)[::-1]):
            if z > max:
                max = z
print(max)
