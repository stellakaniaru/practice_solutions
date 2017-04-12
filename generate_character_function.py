'''Define a function generate_n_chars() that takes in 
an integer n and a character c that returns a string
n characters long,consisting of c's.
eg: (5, 'x') should return 'xxxxx'
'''


def generate_n_chars(x, y):
	n = ''
	for i in range(1,x+1):
		n += y
	return n

