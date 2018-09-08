# Calculate standard deviation 


from functools import reduce 

import math

a = [5,6,11,13,19,20,25,26,28,37]

mean = (reduce(lambda x,y:(x+y),a)) / len(a)

variance = (sum(map(lambda i:(i-mean) ** 2,a))) / len(a)

sd = math.sqrt(variance)

print(variance)
print(sd)