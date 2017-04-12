'''
Define a simple 'spelling correction' function correct()
that takes a string and sees to it that:
1. two or more occurences of the space character is compressed.
2. inserts an extra space after a period if the period is directly
followed by a letter.

E.g:
correct('This  is  very  funny and  cool.Indeed!')

should return:
('This is very funny and cool. Indeed!')

Tip: use regular expressions.
'''

def correct(string):

	#changes the punctuation after a period
	string = string.replace('.', '. ')

	#splits the string into individual words and returns it as a new one with compressed spaces
	string = ' '.join(string.split())
	
	#returns the newly punctuated string
	return string





