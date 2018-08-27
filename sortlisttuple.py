# Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple

a = [(6,100), (8,20), (3,10), (5,50), (1,2)]

b = dict(a)

c = sorted(b.items(), key=lambda b: b[1])

print(b)
print(c)
