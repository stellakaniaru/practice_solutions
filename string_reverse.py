'''
Finds the reverse of the words fed into the program.
'''

#ask user to specify the number of testcases
case = int(raw_input('enter number of cases: '))

#loop through the test cases
for i in range(1,case+1):
	#ask for user input
	case = raw_input('enter test case%d: '%i)
	
	#change input into a list of individual words
	new = case.split()
	
	#reverse the words in the list
	new_l = new[::-1]
	
	#print out the words in reverse order 
	print 'case#%d:'%i,' '.join(new_l)




