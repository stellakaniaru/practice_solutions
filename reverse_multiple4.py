'''
Write a program that reverses a string if its
length is a multiple of 4.
'''

def multiple4(string):
	if len(string) % 4 == 0:
		return string[::-1]
	return string

