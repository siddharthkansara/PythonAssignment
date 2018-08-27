#13. Write a Python program to prove that two string variables of same value point same memory location. 


str1 = 'hello'
str2 = 'hell0'

if id(str1) == id(str2):
	print('same location')
print('Not same')