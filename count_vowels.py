#Count the Number of Vowels in a String

str_1 = 'Wildlife documentaries are awesome'

count = 0

for item in str_1:
	if item == 'a' or item =='e' or item =='i' or item == 'o' or item == 'u':
		count += 1

print(count)
print(str_1[::-1])
