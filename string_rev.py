'''
Using the Python language, have the function FirstReverse(str)
take the str parameter being passed and return the string in 
reversed order. For example: if the input string is 
"Hello World and Coders" then your program should return the 
string "sredoC dna dlroW olleH". 
'''

def FirstReverse(str1):
	#splits string into individual words and places them in a list
	new_str = str1.split()
	#initialize a new list
	r = []
	#initiate a loop to reverse all words and add them to the new list
	for i in new_str:
		r.append(i[::-1])
	#print out the reversed words in a reversed order
	return ' '.join(r[::-1])

