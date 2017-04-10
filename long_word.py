'''
Using the Python language, have the function LongestWord(sen) 
take the sen parameter being passed and return the largest 
word in the string. If there are two or more words that are 
the same length, return the first word from the string with 
that length. Ignore punctuation and assume sen will not be empty. 
'''

#using max function and its optional key argument which takes in a function
def LongestWord(x):
	x1 = x.split()
	lon = max(x1, key=len)
	return lon

