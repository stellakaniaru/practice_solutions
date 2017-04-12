'''
A pangram is a sentence that contains all the letters of
the English alphabet atleast once eg: 'The quick brown fox jumps
over the lazy dog'. Write a function to check a sentence and
see if its a pangram or not.
'''

def pangram(sentence):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
				'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
				'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
				'y', 'z']

	sentence.lower()
	sentence = sentence.split()
	new_sentence = ''.join(sentence)
	for i in alphabet:
		if i not in new_sentence:
			return False
	return True
			
print pangram('The quick brown fox jumps over the lazy dog') 