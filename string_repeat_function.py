'''
Create a function that takes in two parameters where one is 
a string and the other is the number of times which the string
should be repeated.
'''

def string_repeat(x, y):
	if type(x) == str:
		return x * y
	else:
		return 'First parameter should be a string!'

