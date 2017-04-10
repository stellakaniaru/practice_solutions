'''
Write a program to add 'ing' at the end of a given string
(length should be atleast 3). If the given string already
ends with 'ing', add 'ly' instead. If the string length is less 
than 3 leave it unchanged.
'''


def suffix(word):
	if len(word) >= 3:
		if word.endswith('ing') == True:
			return word + 'ly'
		else:
			return word + 'ing'
	else:
		return word

