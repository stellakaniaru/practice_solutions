'''Reading and writing files'''

from sys import argv

script, filename = argv

print "We're going to erase %r."%filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you don't want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

#when you open the file in write mode,you dont need to truncate.
#write erases the contents of the already existing file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now am going to ask you for three lines."

line1 = raw_input("line1: \n")
line2 = raw_input("line2: \n")
line3 = raw_input("line3: \n")


print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#alternatively:
#SEE HOW TO WRITE USING ONE COMMAND

print "And finally we close it."
target.close()