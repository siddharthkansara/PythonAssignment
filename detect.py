#Detect if Two Strings are Anagrams


str_1 = 'elbow'
str_2 = 'below'

a = set(str_1)
b = set(str_2)

if (a.intersection(b) == a ) and (a.intersection(b) == b):
	print('Two strings are Anagrams')
else: 
	print('Not Anagrams')