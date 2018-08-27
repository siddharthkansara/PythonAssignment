#Generate Random Numbers from 1 to 20 and Append Them to the List

import random

a = []

for num in range(1,20):
	
	a.append(random.randint(1,20))
	
print(a)

