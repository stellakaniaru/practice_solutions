'''
Define a function that takes in three numbers as
arguments and returns the largest of them.
'''

#function definition
def max_of_three(x,y,z):
	
	#check if x if the largest
	if x > y and x > z:
		return x

	#check if y is the largest
	elif y > x and y > z:
		return y

	#if the first two conditions arent met,z becomes the largest by default
	else:
		return z
