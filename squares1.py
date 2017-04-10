'''
Write a program to generate and print a list of first and last
5 elements where the values are squares of numbers between 1 and 30
(both included).
'''
square = []
for i in range(1, 31):
	square.append(i ** 2)

first5 = square[0:5]
last5 = square[25:]
print (first5 + last5)