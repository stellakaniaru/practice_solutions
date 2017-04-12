'''
Write a program that maps a list of words into a list of
integers representing the lengths of the corresponding 
words. Write it in three different ways:
1. Using a for loop
2. Using the higher order function map
3. Using a list comprehension
'''

#using a for loop
def map_words(words):
	lengths = []
	for i in words:
		lengths.append(len(i))
	return lengths

print(map_words( ['stella', 'kaniaru', 'rocks']))

#using the map() func
word = ['me']
words = ['stella', 'kaniaru', 'rocks']
lengths = map(len, words)
print(list(lengths))

#using a list comprehension
words = ['stella', 'kaniaru', 'rocks']
lengths = [len(i) for i in words]
print(lengths)


