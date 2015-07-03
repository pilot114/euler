def factorize(num):
    factors = [1, num]
    for i in range(2, int(num**0.5)+ 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num / i)
    return list(set(factors))

def first_triangle_with_divisors(num):
    count = 1
    triangle = 1
    factor_count = 0
    while factor_count < num:
        count += 1
        triangle += count
        if triangle % 2 == 0 and triangle % 3 == 0:
	        factor_count = len(factorize(triangle))
    return triangle

print(first_triangle_with_divisors(500))
