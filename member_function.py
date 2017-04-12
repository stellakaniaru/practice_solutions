'''Define a function is_member() that takes in
a value and a list of items as arguments. Should
return true if the value is in the list. False 
otherwise.
Dont use the in operator.
'''


def is_member(x, a):
	'''Returns True if value x is in
	list a.'''
	for i in a:
		if i == x:
			return True 
	return False



