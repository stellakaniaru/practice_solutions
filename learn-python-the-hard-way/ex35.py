'''Branches and Functions.
A game that involves choices. 
'''

'''FIND OUT HOW TO ENTER INT VALUES.'''

from sys import exit


def gold_room():
	'''Leads you to the room full of treasure.'''
	print( "This room is full of gold. How much do you take?")

	choice = input('> ')
	if type(choice) == int:
		how_much = choice

	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print ("Nice, you're not greedy, you win!")

	else:
		print ("You greedy bastard!")


def bear_room():
	'''Leads you to a room where depending on choice made,
	you can end the game or proceed on to another room.'''
	print ("There's a bear here.")
	print ("The bear has a bunch of honey.")
	print ("The fat bear is infront of another door.")
	print( "How are you going to move the bear?Take honey, taunt bear or open door?")
	bear_moved = False

	while True:
		choice = input('> ')

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print( "The bear has moved from the door. You can go through it now.")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print( "I go no idea what that means.")


def cthulhu_room():
	'''Leads you to one of the rooms where depending on choice made,
	you can end the game or call the start function again.'''
	print ("Here you see the great evil Cthulhu.")
	print ("He, it, whatever stares at you and you go insane.")
	print( "Do you flee for your life or eat your head?")

	choice = input('> ')

	if 'flee' in choice:
		start()
	elif 'head' in choice:
		dead("Well, that was tasty!")
	else:
		cthulhu_room()


def dead(why):
	'''Prints out a statement that leads the player to exit the game,stopping the loop.'''
	print (why, "Good job!")
	exit(0)


def start():
	'''Iniatites the game. Provides two choices which lead to the other functions.'''
	print ("You are in a dark room.")
	print ("There is a door to your right and left.")
	print ("Which one do you take?")

	choice = input('> ')

	if choice == 'left':
		bear_room()
	elif choice == 'right':
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve")


start()