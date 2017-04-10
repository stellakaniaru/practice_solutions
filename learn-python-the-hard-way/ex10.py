'''what was that?'''

#horizontal tab character
tabby_cat = "\t I'm tabbed in."

#new-line character
persian_cat = "I'm split\non a line."

#backlash character
backlash_cat = "I'm \\ a \\ cat."

#combines both tab and new-line characters
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat


#using both escape characters and format strings.
#use of %s
#it interpretes the escape characters and prints out string with expected format
print 'Stella is %s.\n'%'a:\n\t*lovely\n\t*charming\n\t*intelligent young lady'

#using both escape characters and format strings.
#use of %r
#since its used to show raw_input,it shows the string how youve typed it
print 'Stella is %r.\n'%'a:\n\t*lovely\n\t*charming\n\t*intelligent young lady'