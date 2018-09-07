#Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).


a = list(range(1,10))

d = {}

e = d.fromkeys(a)

i = 0

for key in e:
	e[key] = a[i] * a[i]
	i += 1

print(e)