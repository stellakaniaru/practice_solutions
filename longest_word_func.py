'''
Write a function find_longest_word() that takes
a list of words and returns the length of the 
longest one.
'''

#using max function and its optional key argument which takes in a function
def find_longest_word(x):
	lon = max(x, key=len)
	return lon


#using a for loop
def find_longest_word2(x):
	longest = len(x[0])
	for i in x:
		if len(i) > longest:
			longest = len(i)
	return longest





