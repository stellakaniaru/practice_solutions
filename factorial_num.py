'''
Using the Python language, have the function FirstFactorial(num) 
take the num parameter being passed and return the factorial of 
it (e.g. if num = 4, return (4 * 3 * 2 * 1)). The input will always be 
an integer. 
'''

def FirstFactorial(num):
	#factorial of 0 and 1 is 1
	if num <= 1:
		return 1
	else:
		fact = 1
		#multiply all numbers within the range of number provided to get its factorial
		for i in range(1, num + 1):
			fact *= i
		return fact
