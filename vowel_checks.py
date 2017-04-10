'''
Define a function that takes in a character.It returns
True if it a vowel and False if otherwise.
'''

#function definition
def vowel_check(c):
	vowel_list = ['a', 'e', 'i', 'o', 'u']
	if c in vowel_list:
		return True
	return False

