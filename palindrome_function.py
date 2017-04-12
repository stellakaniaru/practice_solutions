'''Define a function is_palindrome() that 
recognises palindromes. It should return True
for palindromes.
'''

def is_palindrome(x):
	if x == x[::-1]:
		return True
	return False


