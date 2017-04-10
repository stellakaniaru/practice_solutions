'''Functions and Files.'''

from sys import argv

script, input_file = argv

#function that displays all file contents
def print_all(f):
	print f.read()

#function that shows the file position in terms of bytes
def rewind(f):
	f.seek(0)

#function that prints out a line and its line number
#readline scans each byte of the code until it finds a \n character.
#It then stops to return what it has found so far.
def print_a_line(line_count, f):
	print line_count, f.readline()

#open the file as an object
current_file = open(input_file)

#prints out all the file contents
print "First let's print the whole file:\n"
print_all(current_file)

#sets the file position to initial position ie 0 byte
print "Now let's rewind, kind of like a tape:"
rewind(current_file)

print "Let's print three lines:"

#variable that holds the line count
current_line = 1
print_a_line(current_line, current_file)

#increments the line count by 1
current_line += 1
print_a_line(current_line, current_file)

#increments the line count by 1
current_line += 1
print_a_line(current_line, current_file)