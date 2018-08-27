#Put Even and Odd elements in a List into Two Different Lists

a = [32,1,34,13,123,4,5,6]
num = 0
b=[]
c=[]
for num in a:
	if (num % 2 == 0):
		b.append(num)
	else: 
		c.append(num)
print(b,c)
