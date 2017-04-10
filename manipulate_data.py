'''
Create a function that takes in a list of numbers and returns the
sum total of negative numbers and the number of positive integers 
in the list. The output should be in a list.
'''

def manipulate(a):
	totalP = 0
	totalN = 0
	
	if type(a) is list:
		for i in a:
			if i >= 0:
				totalP += 1
			else:
				totalN += i
	return [totalP, totalN]


