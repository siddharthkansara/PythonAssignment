#Read a List of Words and Return the Length of the Longest One

a = [ 'am', 'i', 'doing', 'well', 'you?', 'and']
b = []

for item in a:
	b.append(len(item))

c = dict(zip(a,b))

d = dict(sorted(c.items(), key=lambda c: c[1]))

print(d[1])

