'''Functions and Variables.'''
'''there different ways to pass values to the 
function:can be math,variables, straight numbers or a combination.
'''

#define a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" %cheese_count
	print "You have %d boxes of crackers!" %boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

#pass values to the function using direct numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#pass values to the function using variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#pass values to the function using math
print "We can even do math inside too!:"
cheese_and_crackers(10 + 20, 30 + 48)

#pass values to the function using both variables and math
print "AND we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 26, amount_of_crackers + 37)
