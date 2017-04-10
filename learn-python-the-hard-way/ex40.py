'''Modules, Classes and Objects'''

class Song(object):

	#initializes the class with its attributes
	def __init__(self, lyrics):
		self.lyrics = lyrics

	#a class method that can be called to perform a specified action	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

#instantiates the class
happy_bday = Song(['Happy birthday to you',
					'I don\'t want to get sued',
					'So I\'ll stop right there'])

#instantiates the class
bulls_on_parade = Song(['They rally around the family',
						'With pockets full of shells'])

worship1 = Song(['Umejiumbia',
				'Malaika wakuabudu',
				'Ndio maana mimi nasema',
				'Uabudiwe!'])

#calls on the class method
happy_bday.sing_me_a_song()
print '-' * 10
bulls_on_parade.sing_me_a_song()
print '-' * 10
worship1.sing_me_a_song()

