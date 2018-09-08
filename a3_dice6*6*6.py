#dice 6*6*6


from collections import Counter,OrderedDict


a = [1,2,3,4,5,6]

c = [(n,x,y) for n in a for x in a for y in a] # this is making 6*6*6 list with all combinations totalling to 216

#print(c) 

d = list(map(lambda i: sum(i),c))

e = Counter(d)

print(e) #this will just print unordered dictionary.

print(OrderedDict(sorted(e.items()))) #this will sort it.
