'''
Define a function reverse() that should 
return the reverse of a string.
'''

#using the reverse keyword
def reverse(x):
	return x[::-1]

print(reverse('I am testing'))



#using a loop
def reverse2(a):
	#new list
	d = []

	i = len(a)
	while i:
		i -= 1
		d.append(a[i])
	return ''.join(d)





#raw code
r = 'winnie'
print (''.join(reversed(r)))
