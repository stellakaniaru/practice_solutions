'''
The song 99 bottles of beer is a traditional song in the US and Canada.
It has a very repetitive format thats easy to memorize. The lyrics are 
as follows:

'99 bottles of beer on the wall, 99 bottles of beer. Take one down,
pass it around, 98 bottles of beer on the wall.'

The same verse is repeated each time less one bottle. The song 
ends once the singers reach zero.

Write a program capable of generating all the verses of the song.
'''

num_bottles = list(range(1, 100))
num_bottles= num_bottles[::-1]


for i in num_bottles:
	remainder = i - 1
	if i == 1:
		print('''
		%r bottles of beer on the wall, %r bottles of beer.
		Take one down,pass it around, no more beer on the wall!
	'''%(i, i))
		

	else:
		print('''
	%r bottles of beer on the wall, %r bottles of beer.
	Take one down,pass it around, %r bottles of beer on the wall!

	oohh!
	'''%(i, i, remainder))




