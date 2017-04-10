'''While loops.'''

'''The loop as it is.'''
#initializes i at 0
i = 0

#creates an empty list to hold values
numbers = []

#loops while condition evaluates to true
while i < 6:
	#prints out the value of i at the beginning of each loop
	print "At the top i is %d" % i

	#stores the values generated from the loop in the list assigned to variable numbers
	numbers.append(i)

	#increments the value of i by 1 after every loop
	i += 1 

	#prints the values added to the list after each loop
	print "Number's now: ",numbers

	#prints out the value to be checked on the next loop after i is inremented
	print "At the bottom i is %d" % i

print "The numbers: "

#loops through all the values in the list and prints them out
for num in numbers:
	print num




def wloop(increament, count):
'''The while loop as a callable function.'''
	i = 0
	numbers = []

	#test is replaced by a variable which is the function argument
	while i < count:
		#prints out the value of i at the beginning of each loop
		print "At the top i is %d" % i

		#stores the values generated from the loop in the list assigned to variable numbers
		numbers.append(i)

		#increments the value of i by increment value given in the argument after every loop
		i += increament 

		#prints the values added to the list after each loop
		print "Number's now: ",numbers

		#prints out the value to be checked on the next loop after i is inremented
		print "At the bottom i is %d" % i

	print "The numbers: "

	#loops through all the values in the list and prints them out
	for num in numbers:
		print num


print wloop(2, 6)


def wloop2(count):
	'''evaluates the while loop using for-loop and range.'''
	i = 0
	for i in range(count):
		print i
		


print wloop2(4)