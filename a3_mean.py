#calculate mean average

from functools import reduce 


a = [3,5,2,7,8,9,10]

b = (reduce(lambda x,y:(x+y),a))

print(b/len(a))

