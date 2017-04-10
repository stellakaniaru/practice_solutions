'''Names, Variables, Code, Functions.'''

#function that makes use of args variable
def print_two(*args):
	arg1, arg2 = args
	print 'arg1 : %r, arg2 : %r' %(arg1, arg2)

#a redo of the first function with specific arguments	
def print_two_again(arg1, arg2):
	print 'arg1 : %r, arg2 : %r' %(arg1, arg2)

#function with one argument
def print_one(arg1):
	print 'arg1 : %r' %(arg1)

#function without any arguments
def print_none():
	print 'I got nothing.'

