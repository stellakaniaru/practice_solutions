'''
Write a function char_freq() that takes a string and
builds a frequency listing of the characters contained in
it. Represent the frequency listing as a python dictionary.
Try it with something like char_freq('abbabcbdabdbdbababababcbcbcbab')
'''

#class Counter(__builtin__.dict)
   #Dict subclass for counting hashable items.  Sometimes called a bag
   #or multiset.  Elements are stored as dictionary keys and their counts
  #are stored as dictionary values.
from collections import Counter

def char_freq(word):
	count = dict(Counter(word))
	return count

