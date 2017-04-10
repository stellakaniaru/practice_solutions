'''more variables and printing'''

name = 'Stella Kaniaru'
age = 19 #not a lie
height = 70 #inches
weight = 150 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Short and black'

#converting pounds to kilograms
new_weight = 150 * 0.45359237

#converting inches to centimeters
new_height = 70 * 2.54

print "Let's talk about %s."%name
print "She is %d inches tall.(%d centimeters)"%(height, new_height)
print "She is %d pounds heavy.(%d kilograms)"%(weight, new_weight)
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair."%(eyes, hair)
print "Her teeth are usually %s depending on the coffee."%teeth

#this line is tricky,try to get it exactly right
print "If I add %d, %d and %d I get %d."%(age, height, weight, age + height + weight)

