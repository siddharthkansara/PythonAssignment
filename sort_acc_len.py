#Sort a List According to the Length of the Elements

a = ['hello', 'brother','from', 'another','mother']


b = []

for item in a:
	b.append(len(item))

c = dict(zip(a,b))

d = dict(sorted(c.items(), key=lambda c: c[1]))


e = []

for key in d:
	 e.append(key)


print(e)







