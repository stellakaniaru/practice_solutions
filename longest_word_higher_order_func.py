'''
Write a function find_longest_word() that takes a word and
returns the length of the longest one.
Use only higher order functions.
'''

def find_longest_word(words):
	longest = max(words, key=len)
	return len(longest)

