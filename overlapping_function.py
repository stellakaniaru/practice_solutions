'''Define a function overlapping() that takes in 
two lists and returns True if they have one member 
in common. False otherwise. Use two nested for loops.
'''

def overlapping(x, y):
	'''loops through two lists to return True if they 
	have a common member. Otherwise returns False.'''
	for i in x:
		for j in y:
			if i == j:
				return True
	return False

