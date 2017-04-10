'''parameters, unpacking variables'''

from sys import argv

feedback = raw_input('Do you know what the arg variable is? ')

#argv is an argument variable
#arguments in argv are unpacked in the left
#argv holds arguments you pass to your script on running it
script, first, second, third = argv

print "The script is called:",script
print "Your first variable is:",first
print "Your second variable is:",second
print "Your third variable is:",third

