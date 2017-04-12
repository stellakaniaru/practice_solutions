'''
Using the higher order function reduce(), write a function
max_in_list() that takes a list of numbers and returns the 
largest one. Ask yourself why define a new function when you
can just call the reduce() function directly.
'''

'''
You need to have a defined function since its an argument
needed in the reduce function. i.e:
reduce(func, sequence, [initial])
'''
from functools import reduce

max_in_list = lambda a, b:a if (a > b) else b
print(reduce(max_in_list, [12, 45, 567, 89, 23]))




