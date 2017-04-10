'''
Using the Python language, have the function 
LetterCapitalize(str) take the str parameter being 
passed and capitalize the first letter of each word. 
Words will be separated by only one space
'''

def LetterCapitalize(str1):
	new = str1.split()
	fresh = []
	for i in new:
		fresh.append(i.capitalize())
	return ' '.join(fresh)

