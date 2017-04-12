'''
Write a program that prompts the user to enter a password 
before accessing their account.
'''

'''
1. Prompt user to register.
2. Store password for future cross checking.
3. Prompt user to enter their password.
4. Cross check password and if found grant acccess.
'''

print ('''
	Hello there! Welcome to my website. My name is Stella.
	Am really excited to have you here.
	We will be really good friends.
	First, you'll have to sign up inorder to register as my friend.
	Kindly follow the prompts below.
	Remember to have fun!! :) ;)
	''')

name = input('I\'d love to know your name: ')
password = input('Kindly set your password to protect your data: ')



print ('To log into your account, kindly fill in your name and your password.')

user_name = input('Name: ')
user_password = input('Password: ')

if name != user_name or password != user_password:
	print ('Invalid username or password!')
else:
	print ('You have successfully logged in!\n We are officially mates!! :) :)')