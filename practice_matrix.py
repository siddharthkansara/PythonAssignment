import random

nums = [0,1,2]

c = []
r_nums1 = []
r_nums2 = []

c = [(a,b) for a in nums for b in nums]

r_nums1 = [4,2,6,9,7,4,5,6,1,2]

#r_nums1 = [random.randint(1,10) for n in range(10)]

M1 = (list(zip(c,r_nums1)))

#r_nums2 = [random.randint(10,20) for n in range(10,20)]

#M2 = dict(zip(c,r_nums2))


print(M1[5][1])
print(M1)

