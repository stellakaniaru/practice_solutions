'''strings and text'''

#display number of people
x = 'There are %d types of people.'%10

#variable binary
binary = 'binary'

#variable do_not equated to its short form
do_not = "don't"

#variable holding a statement with variables
#string put inside a string
y = "Those who know %s and those who %s."%(binary, do_not)

#prints out statement in variable x
print x

#prints out statement in variable y
print y

#print out x
#string put inside a string
print "I said: %r"%x

#print out y
#string put inside a string
print "I also said: %s"%y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#joins the two variables
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#joins two variables
print w + e
