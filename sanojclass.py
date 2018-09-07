a = list(map(int,input('Enter List:').split()))
b = int(input('Enter the number to be found: '))
c = 0
for num,index in enumerate(a):
	if b == num:
		c = 1

	else:
		continue

if c == 1:
	print('Found at')
elif c == 0: 		
	print('Not found')


