from itertools import product
import csv

#the number without the last four digits
num = "+44737526"

#range in which to look for combinations
numList = range(0,10)

#list to store contacts
contacts = []

#find all posible combinations of the last four numbers
d = ["".join(map(str, comb)) for comb in product(numList, repeat=4)]

#create a contact list with all possible combinations and store in a list
for i in d:
    contacts.append([i, num+i])
	


#generate a csv file to store the contacts
with open('contacts.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(contacts)

csvFile.close()


#convert the csv file into a vcard
with open( 'contacts.csv', 'r' ) as source:
	reader = csv.reader( source )
	allvcf = open('ALL.vcf', 'w')
	i = 0
	for row in reader:
		#write in the "ALL.vcf" file
		allvcf.write( 'BEGIN:VCARD' + "\n")
		allvcf.write( 'VERSION:3.0' + "\n")
		allvcf.write( 'N:' + row[0] + ';' + "\n")
		allvcf.write( 'FN:' + row[0] + ' ' + "\n")
		allvcf.write( 'TEL;CELL:' + row[1] + "\n")
		allvcf.write( 'END:VCARD' + "\n")
		allvcf.write( "\n")

		
	allvcf.close()
	
        
#on the icloud account,import the vcard file
