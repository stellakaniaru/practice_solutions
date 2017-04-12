'''
Write a function translate() that will translate a text into
"rovarsparaket",Swedish for robbers language. That 
is, double every consonant and place an
occurence of "o" in between. Example: 'this' becomes 'tothohioisos'
'''

def translate(x):
	new = ''
	for i in x:
		if i  in 'bcdfghjklmnpqrstvwxyz':
			new += i + 'o' + i
		else:
			new += i
	return new
	
			
