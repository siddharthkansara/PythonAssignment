a = list(range(1,30))

c = []
d = []

def lala(n):
	
	for num in a:
		if num%2 == 0:
			c[i] = a.pop(num)

	
	
a1= list(map(lala,a))

print(a1)
print(c)




'''
for n in a:
	if n%i == 0:
		a.remove(n)
i += 1
b.append(a[0])

#print(b)

for n in a:
	if n%i == 0:
		a.remove(n)
i += 1
b.append(a[0])

#print(b)
#print(a)
'''
'''
c = (n for n in a if n%2 != 0) # generator comprehension

for i in c:
	print(i)

#d = list(range(1,30))
i = 1
#b.append(a[0])
for n in a:
	print(n)
	if n%i == 0 and n == i:
			b.append(n)
		i += 1
		#else:
			#a.remove(n)
	i = 1	
		#a.remove(n)

#print(a)
print(b)

'''


