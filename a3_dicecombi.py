#dice 6*6*6


from collections import Counter,OrderedDict


a = [1,2,3,4,5,6]

c = [(n,x,y) for n in a for x in a for y in a]

#print(c)

d = list(map(lambda i: sum(i),c))

e = Counter(d)

print(e)

print(OrderedDict(sorted(e.items())))
