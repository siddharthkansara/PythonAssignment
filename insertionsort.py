#sort using selection method

a = list(map(int,input('Enter List:').split()))

for i in range(len(a)):
	for j in range(len(a)-1):
		if a[i] < a[j]:
			a[i],a[j]=a[j],a[i]

print(a)