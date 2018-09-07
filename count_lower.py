#Count Number of Lowercase Characters in a String

str_1 = 'HelloBro'

count = 0 


for item in str_1:
	if item==str_1.islower():
		count += 1

print(count)

