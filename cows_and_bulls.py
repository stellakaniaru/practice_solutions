'''
Create a program that will play the cows and bulls game with 
the user. The game works like this:
Randomly generate a 4-digit number.Ask the user to guess a 4-digit
number. For every digit that the user guessed correctly he gets a 
'cow' and for every digit the user guessed wrongly, he gets a 'bull'.
Once a user guesses a a number,tell the how many cows and bulls they 
have.Keep track of the number of guesses the user makes and tell them
at the end. The game ends when the user guesses the correct number.
'''

import random

num = str(random.randint(1000, 9999))

user_num = input('Guess any four digit number: ')
bulls = 0
cows = 0

def check():
	if num[0] != user_num[0]:
		print ('bull')
		bulls += 1
	else:
		print ('cow')
		cows += 1
	if num[1] != user_num[1]:
		print ('bull')
		bulls +=1
	else:
		print ('cow')
		cows += 1
	if num[2] != user_num[2]:
		print ('bull')
		bulls +=1
	else:
		print ('cow')
		cows += 1
	if num[3] != user_num[3]:
		print ('bull')
		bulls +=1
	else:
		print( 'cow')
		cows += 1

print('%r bulls, %r cows'%(bulls, cows))
	
while num != user_num:
	print('Guess a four digit number:')
	user_num = input()



# a = str(1234)

# b = str(1342)

# if a[1] == b[1]:
# 	print 'cow'
# print 'bull'