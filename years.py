'''
Create a program that asks the user to enter their name and 
age. Print out a message addressed to them that tells them
the year they will turn 100 years old.
'''

from datetime import date

#ask for user input on name and age
name = input('Enter your name: ') 
age = int(input('Enter your age: '))
num = int(input('Enter a number to show how many times the output should be printed: '))
#generates the current year
years = date.today().year

#generates the year of birth
diff = years - age

#generates the year the individual will turn 100 years
a_100 = diff + 100

#outputs the results 
print("%s, you will be a 100yrs in the year %s\n" %(name, a_100) * num)