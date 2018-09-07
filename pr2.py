a = list(map(int,input('Enter List:').split()))
b = int(input('Enter the number to be found: '))
c = 0
l = 0
m = 0 
u = len(a)-1

while l <= u:
	m = (l+u) // 2

	if (a[m] == b):
		c = 1
		print('Found at', m+1)
		break

	elif (b > a[m]):
		l = m + 1
		
	else:
		u = m - 1	

