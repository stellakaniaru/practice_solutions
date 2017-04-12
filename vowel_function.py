'''Define a function that takes in a character.
It returns True if its a vowel and False if otherwise.
'''

def check_vowel(v):
	group = ('a', 'e', 'i', 'o', 'u')
	v = v.lower()
	if v in group:
		return True
	return False

print(check_vowel('A'))
print (check_vowel('a'))

