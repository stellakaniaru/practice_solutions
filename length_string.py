'''
Define a  that computes the length of a given
list or string. Don't use the len function.
'''

def length(x):
	'''Returns the length of the given argument.'''
	len_ = 0
	for i in x:
		len_ += 1
	return len_

