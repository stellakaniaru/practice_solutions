'''A test to run ex19 function lesson.'''

def add(num1, num2):
	total = num1 + num2
	print "Answer is %r\n" %total


#feed the values directly
print 'We can feed the values directly:'
add(12, 45)

#feed the values using variables 
print 'We can feed the values using variables:'
x = 67
y = 35

add(x, y)

#feed the values using math
print 'We can feed the values using math:'
add(12 + 4, 23 + 4)

#combine both math and variables
print "We can combine both math and variables:"
add(x + 12, y + 1000)

#ask for user input
print "We can ask for user input:"
a = int(raw_input(""))
b = int(raw_input(""))

add(a, b)