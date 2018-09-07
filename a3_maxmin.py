# Maximum and minimum


a = [51,20,4,91,1,73,3,10,98,45]

counter = 0 

for i in range(len(a)):
	for j in range(len(a)):
		if a[i]>a[j]:
			counter += 1

	if counter == (len(a)-1):	
		print('Max -->',a[i])
		break
	else:
		counter = 0

counter = 0 

for i in range(len(a)):
	for j in range(len(a)):
		if a[i]<a[j]:
			counter += 1

	if counter == (len(a)-1):	
		print('Min -->',a[i])
		break
	else:
		counter = 0