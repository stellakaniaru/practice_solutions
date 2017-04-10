'''Reading files'''

#imports the argv variable from the sys module
from sys import argv

#assigns arguments to argv
script, filename = argv

#txt variable holds the file object
txt = open(filename)

#print out a simple message with the filename
print "Here's your file %r: "%filename

#the read method displays the contents(reads) in the file object
print txt.read()

#prompt user to type in the filename again
print "Type the filename again: "
file_again = raw_input("> ")

#assign variable to hold the new file object
txt_again = open(file_again)

#read the file object contents and display them
print txt_again.read()
