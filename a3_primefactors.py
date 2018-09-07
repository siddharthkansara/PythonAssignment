#prime factor of a number 

num = int(input('Enter a number: '))
a = []
for i in range(2,round(num*0.5)):
	if num%i ==0:
		a.append(i)
for i in a:
	if i%2==0:
		i = ''

print(a)
print(set(a))
