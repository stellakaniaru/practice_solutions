'''Define a function max_in_list() that returns the maximum value 
from any list given.'''


def max_in_list(x):
	Max = x[0]

	for i in x:
		if i > Max:
			Max = i
	return Max


