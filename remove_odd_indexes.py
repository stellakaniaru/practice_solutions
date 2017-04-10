'''
Write a program to remove the characters that have odd
index values of a given string.
'''
name = 'stella' 
def name_odd(name):
	f = len(name)
	new = ''

	for i in range(0, f ):
		# print(name[i])
		if i % 2 == 0:
			new += name[i]
	return new

