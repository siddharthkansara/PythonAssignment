#Calculate median 


a = [21,45,32,44,67,89,90,95,100,11]

a.sort()

print(a)

if len(a)%2 ==1:
	b =int((len(a)+1)/2)
	print(a[b-1])
elif len(a)%2 ==0:
	b = int((len(a))/2)
	c = int((len(a)+1)/2)
	d = (a[b-1] + a[c])/2
	print(d)

	