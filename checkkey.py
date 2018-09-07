#check if a given key exist in dictionary or not 

d = {'john': 25, 'lia' : 30, 'ram': 43, 'Raghu': 21}

print(d.get('ramu', 'Not Found'))

#another way to see if a key is present in a dic or not

if not 'ramu' in d:
	print('\nmissing')
