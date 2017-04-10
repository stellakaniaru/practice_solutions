'''
Define a function that takes in two lists and returns True 
if they have one member in common.False if otherwise.
Use two nested for loops.
'''

#function definition
def overlapping(list1, list2):

	#loop through items in first list
	for i in list1:

		#loop through items in second list
		for j in list2:

			#check if any of the items in list1 are equal to any of the items in list2
			if i == j:
				return True
	#outside loop to ensure its not caught up in any loop conditions
	return False

