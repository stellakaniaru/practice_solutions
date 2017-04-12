'''
Write a version of palindrome recognizer that also accepts phrase 
palindromes such as 'Go hang a salami I'm a lasagna hog', 'Step on
no pets', 'Rise to vote sir', Satan, oscillate my metallic sonatas
etc.Note that punctuation, capitalization
and spacing are usually ignored.
'''

import string

def phrase_palindrome(x):
	x = x .lower()
	phrase = x.split()
	translator = str.maketrans('', '', string.punctuation)
	new_phrase = ''.join(phrase)
	new_phrase2 = new_phrase.translate(translator)
	n = new_phrase2[::-1]
	if new_phrase2 == n:
		return True
	else:
		return False



