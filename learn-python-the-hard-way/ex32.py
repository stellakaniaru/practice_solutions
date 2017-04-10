'''Loops and Lists.'''

#list with integer values
the_count = [1, 2, 3, 4, 5]

#list with string values
fruits = ['apples', 'oranges', 'pears', 'apricots']

#list with mixed values
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#unpacking list with integer values
for number in the_count:
	print "This is count %d"%number

#unpacking list with string values
for fruit in fruits:
	print "A fruit of type:%s"%fruit

#unpacking list with mixed values
for i in change:
	print "I got %r"%i

#initializing an empty list
elements = []

#adding elements to empty list using append method
for i in range(0, 6):
	elements.append(i)

#looping through the list to print out added values
for i in elements:
	print "Element was: %d"%i