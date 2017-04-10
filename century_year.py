'''
Create a program that asks the user to enter their name and age.
Print out a message addressed to them that tells them the year
they will turn a 100 yrs old.
'''
import datetime


#prompt user to enter name and age
name = input('Enter name: ')
age = int(input('Enter age: '))

#get the current year
year = datetime.datetime.now().year

#find the users birth year
birth_year = year - age

#find year the user turns a 100 yrs
century_year = birth_year + 100

#tell user the year they turn a 100 years
print ('{}, you will turn a 100yrs in the year {}'.format(name, century_year))

# help('datetime')

