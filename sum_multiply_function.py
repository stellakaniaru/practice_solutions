'''Write a function sum() and multiply() that adds and
multiplies numbers in a list repectively.
'''


def sum_(x):
	'''Returns the sum of numbers in a list'''
	tot = 0
	for i in x:
		tot += i
	return tot

def multiply(x):
	'''Returns the product of numbers in a list.'''
	tot = 1
	for i in x:
		tot *= i
	return tot

