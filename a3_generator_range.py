#generator range


a = (num for num in range(10)) # 'a' has become a generator object in this. this is generator comprehension

print(next(a),'First element') # this prints just the first element.

for num in a:				   # this loops through 'a'
	print(num)

print(a)					   # this prints the address of memory object 'a'
