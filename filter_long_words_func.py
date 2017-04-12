'''
Write a function filter_long_words() that takes a list 
of words and an integer n and returns the list of words
that are longer than n.
'''

#using a for loop
def filter_long_words(words, n):
	new = []
	for i in words:
		if len(i) > n:
			new.append(i)
	return new


#using lambda and filter functions
def filter_long_words2(words, n):
	u=list(filter(lambda i: len(i) > n, words))
	return u

