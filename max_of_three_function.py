'''
Define a function max_of_three() that
takes in three numbers as arguments and returns
 the largest of them.
'''

def max_of_three(x, y, z):
	'''Takes in 3 arguments and returns
	the largest among them.'''
	if x > y and x > z:
		return x
	elif y > x and y > z:
		return y
	else:
		return z

