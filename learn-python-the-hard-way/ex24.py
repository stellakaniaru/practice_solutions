'''More practice.'''

#practice on escape characters
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "----------"
print poem
print "----------"

#practice on mathematical execution
five = 10 - 2 + 3 - 6
print "This should be five: %s" %five

#function to calculate number of beans,jars and crates using a starting figure
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

#variable to hold the starting figure
start_point = 10000

#variable to hold the value after function execution
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" %(start_point)
print "We'd have %d beans, %d jars, and %d crates.\n" %(beans, jars, crates)

#alternatively,we can use the function execution directly instead of assigning it a variable
start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." %secret_formula(start_point)

