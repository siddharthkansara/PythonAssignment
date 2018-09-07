
'''a = 10 

def func(name):
	global a 
	a = 20 
c = func(1)

print(a)'''

'''c = 40

def parentfunction():
	a = 10
	b = 20

	def childfunction():
		global c 
		#print(a)
		#a = 50
		c = 30
		#return c

	#print(a)
	print(childfunction())

parentfunction()
print(c)'''

'''def defarg(x=0, y=10,z=10):
	print(x,y,z)

defarg(10)
defarg()
defarg(7,3,3)
defarg(4,6)'''

'''def avg(*rest):

	l = len(rest)
	print(rest)
	print('Length of rest', l)
	for i in range(0,1):
		print(rest[i])

avg(2,3,4)'''


'''g = lambda x :  x+10 

v = g(100)

print(v)'''

'''def g(x):

	return x ** 2

# dictionary comprehension 
y = { x : g(x) for x in range(10)}

print(y)'''

'''
# passing arguments as lists and dictionary
def foo(*args, **kwargs):
	print(args)
	print(kwargs)

foo(1,2,5, x = 3, y = 4)

'''

# mapping 
'''
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

temp = (36.5, 37, 37.5,39)

l = list(map(fahrenheit,temp))

print(l)
'''
'''
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print(result)
'''
'''
import functools

r = functools.reduce(lambda x,y: x+y, [47,11,42,13])
print(r)
'''

#L = [1,2,3,4]
#it = iter(L)
#print(it)
#print(it#.__next__())

#print(next(it))

print(2 % 2)


