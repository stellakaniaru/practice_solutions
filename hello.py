'''
Welcomes user to the amazing world of the awesome
dynamic experience of using python.
'''


name = input('Enter name: ')

message = '''
		Hello {}! Welcome to the amazing world of python.
		If you are ready for an adventure, strap on your shoes
		and hold on cause youre in for the ride of your life!
		This will be a ride to remember!
		'''.format(name)

print (message.upper())