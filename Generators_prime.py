# Generate prime numbers (using generators)

a = list(range(2,10))
b = []
c = []
i = 0

for n in a:
	#if n % 2 != 0 :
	#	b.append(n)
	b.append(n)
	
	for b in enumerate(a):
		c[i] = a[i] / b[i]
		i += 1
	a = b
print(b)	