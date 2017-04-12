'''
Represent a small bilingual lexicon as a python dict in the following
fashion:
{'merry' : 'god', 'christmas' : 'jul', 'and' : 'och', 'happy' : 'gott',
'new' : 'nytt', 'year' : 'ar'}
and use it to translate your english christmas card into swedish.
Write a function translate() that takes a list of english words and returns a list 
of swedish words.
Use the higher order function map().
'''

#using a function
def translate(sentence):
	transdict = {'merry' : 'god', 'christmas' : 'jul', 'and' : 'och', 'happy' : 'gott',
				'new' : 'nytt', 'year' : 'ar'}

	#splits the sentence into individual words
	sentence = sentence.split(' ')

	#returns the value of each key found in the sentence
	new = [transdict[i] for i in sentence]
	
	#returns a new string comprising of the key values
	return ' '.join(new)



#using map function
def translate(sentence):
	words = {'merry' : 'god', 'christmas' : 'jul', 'and' : 'och', 'happy' : 'gott',
	'new' : 'nytt', 'year' : 'ar'}
	new_s = map(lambda w: words[w], sentence.split(' '))
	return ' '. join(new_s)
	


#using raw code
words = {'merry' : 'god', 'christmas' : 'jul', 'and' : 'och', 'happy' : 'gott',
'new' : 'nytt', 'year' : 'ar'}
sentence = 'merry christmas and happy new year'
new_s = sentence.split(' ')
g = [words [w] for w in new_s]
print(' '.join(g))
