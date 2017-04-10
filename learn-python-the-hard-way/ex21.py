'''Functions can return something.
The return function.
'''

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" %(a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" %(a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" %(a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d\nHeight: %d\nWeight: %d\nIQ: %d\n" %(age, height, weight, iq)

#a puzzle for extra credit
#it makes use of the BODMAS concept to do the calculation.However the calculations are done from th inside out.
#all the other functions are embedded in one function in that all the functions in the brackets have to be executed,
#before the function outside the brackets is executed.
print "Here is a puzzle."

what = multiply(age, add(height, subtract(weight,divide(iq, 2))))
print "multiply(age, add(height, subtract(weight,divide(iq, 2))))"

print "That becomes:", what, "Can you do it by hand?\n"

print "The normal formula would be:"
what1 = age *( height + weight - iq / 2)
print "age *( height + weight - iq / 2)"
print "That becomes:", what1
