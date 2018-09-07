# Decorators examples


'''
def decorator(m):
    print("I'm a decorator")

    def dfunc():
    	print("I'm inner func")
    	m()

    return dfunc


@decorator
     
def my_function():
    print("I'm a function")

my_function()


'''

def repeater(foo):

	def newfoo(*args):
		foo(*args)
		foo(*args)
	
	return newfoo

@repeater
def multiply(x,y):

	print (x * y)

multiply (2,3)

















