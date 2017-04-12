'''
Write a program that maps a list of words into
a list of integers representing the lengths of
the corresponding words.
'''

#using a for loop
def words(x):
	lengths = []
	for i in x:
		lengths.append(len(i))
	return lengths


#using the map function
def word1(x):
	return list(map(len, x))


#using a list comprehension
def word2(x):
	return [len(i) for i in x]


