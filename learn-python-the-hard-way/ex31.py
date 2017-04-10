'''Making decisions.'''

name = raw_input('What is your name mate? ')
print "\tHello there!Welcome to my mystical world. I'll take you on an adventure of this land. But be warned. The sites you view will be dependent on the choices you make."
print "\tLet's begin our quest then!\n"
print "You enter a dark room with two doors. Do you go through door #1 or door #2?\n"

door = raw_input('> ')

if door == '1':
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1.Take the cake."
	print "2.Scream at the bear."

	bear = raw_input('> ')

	if bear == '1':
		print "\nThe bear is caught off guard. He looks at you. You look back. The staring game lasts for a few seconds."
		print "Suddenly,the bear growls. You run away and come upon a coffin. What will you do?"
		print "1. Jump inside and squeeze in with the corpse."
		print "2. Keep on running into the darkness and face the unknown."

		choice = raw_input('> ')

		if choice == '1':
			print "\nThe bear cruises past you and you breath a sigh of relief."
			print "However, you feel an arm on you. The corpse is alive!"
			print "What do you do?"
			print "1.Jump out the coffin and run away screaming!"
			print "2.Punch the corpse."
			print "3.Stay there and die."

			choice1 = raw_input('> ')

			if choice1 == '1':
				print "\nYou are one big coward!Hope you don't run into the bear, hehehe!"

			elif choice1 == '2' or choice1 == '3':
				print "\nIts you against the dead. Quick remainder,you can't kill the dead!You are in some hot soup friend!"
			else:
				print "\nLearn to follow instructions %s!" %name


		elif choice == '2':
			print "\nYou come across a path that branches off into two directions."
			print "Which road will you pick?A or B?"

			road = raw_input('> ')

			if road == 'A':
				print "\nAs you walk along, a eerie sound, like creepy music starts to play."
				print "It seems close at one point and at the next point,it sounds as if its coming from far away."
				print "A branch creaks. You are being followed."
				print "Could it be the bear?"
				print "What will you do?"
				print "1.Keep on walking."
				print "2.Drop down and act dead."

				choice3 = raw_input('> ')

				if choice3 == '1':
					print "\nAfter taking a few more steps,you come face to face with the creature you are running away from."
					print "You are about to discover its identity in the dark."
					print "Just when you are about to call out its name....."
					print "WAKE UP %s!GOSH,DON'T YOU TALK IN YOUR SLEEP. hahahaha...." %name

				if choice == '2':
					print "Be careful what you wish for."
					print "The ground starts to move.Its alive."
					print "And what's even worse,it's swallowing you up whole!"
					print "You try to scream but you seem to have lost your voice."
					print "And then suddenly,you let out a big one loud enough to waken the dead."
					print "%s! DID YOU HAVE THAT BAD DREAM AGAIN?....hehehe....." %name

			if road == 'B':
				print "\nYou drop down into an endless pit,land on a pile of knives and die. RIP %s!"%name

	if bear == '2':
		print "\nThe bear growls.It's about to charge."
		print "You really messed this one up."
		print "You are trapped. You have two options."
		print "1.Sing it a lullaby and hope its drifts off to sleep."
		print "2.Wet your pants and hope its not up for a stinky meal."

		option = raw_input('> ')

		if option == '1':
			print "\nI hope you have an angelic voice cause you are going to need it."
			print "You start singing."
			print "And it just looks at you blankly."
			print "You must really suck."
			print "It outstretches its arm and swings it in for the hit."
			print "You close your eyes and just when your face comes into contact with its fur..."
			print "%s!. WAKE UP.YOU HAVE DETENTION FOR DOZING OFF IN CLASS,AGAIN!"%name

		elif option == '2':
			print "\nYou are shaking like a leaf on a windy day."
			print "It raises up its nose to find out the source of the stench."
			print "And it fixes its eyes on you."
			print "Turns out the bear hates music!"
			print "It opens its mouth.You're going to supplement its snack."
			print "And just when you can smell its foul breath on your face..."
			print "%s ! MOVE!THIS IS A BANK,NOT YOUR BED!"%name
	# 	print "The bear eats your face off. Hahaha! Better luck next time."
	# elif bear == '2':
	# 	print "The bear eats your legs off. Poor you! Better luck next time."
	# else:
	# 	print "Well, doing %s is probably better.The bear runs away."%bear

elif door == '2':
	print "\nYou stare into the endless abyss at Cthulhul's retina."
	print "1.Blueberries."
	print "2.Yellow jacket clothespins."
	print "3.Understanding revolvers yelling melodies."

	insanity = raw_input('> ')

	if insanity == '1' or insanity == '2':
		print "Your body survives powered by a mind of jello. Lucky you!"
	else:
		print "The insanity rots your eyes into a pool of muck. Hahaha! Better luck next time."


else:
	print "You just chose to stay where you are."
	print "Whatever happened to your spirit of adventure mate?"
	print "Good luck!"






