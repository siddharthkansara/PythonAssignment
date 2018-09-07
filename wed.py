#sort using bubble method

a = list(map(int,input('Enter List:').split()))

for i in range(len(a)):
	for j in range(len(a)-1):
		if a[j] > a[j+1]:
			a[j],a[j+1]=a[j+1],a[j]
			
print(a)