'''More files.
Writes the contents in one file to second file.
'''
'''TRY AND MAKE IT ONE LINE LONG'''

#imports functions to use from other packages
from sys import argv
from os.path import exists

#assigns arguments to the argument variable
script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

#we can do the following in two lines. how?
#opens the first file object
in_file = open(from_file)

#reads the file object contents and displays them as standard output
indata = in_file.read()

#prints out the len of the file contents
print "The input file is %d bytes long" %len(indata)

#the exist command checks if a file exists or not based on its name
print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTR-C to abort."
raw_input()

#opens the second file object in write mode
out_file = open(to_file, 'w')

#writes the contents in first file to the second file
out_file.write(indata)

print "Alright, all done."

#closes the files
out_file.close()
in_file.close()