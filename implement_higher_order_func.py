'''
Implement the higher order functions map(), filter()
and reduce().
(Writing them yourself may be good practice though they are
in-built)
'''
from functools import reduce
'''
Filter: Takes a function and an iterable and produces
an output list of every item on the input list that 
passes a test.
'''

def greater_than(x):
	if x > 6:
		return x


print(list(filter(greater_than, range(10))))


'''
Map: Takes an input iterable of values and returns a list 
with different values.Same order,same length but mapped
via a function.
'''
def triple(x):
	return x * x * x

print(list(map(triple, (2, 3, 4, 5, 6))))


'''
Reduce: Takes an iterable of input data and consumes it
from left to right to come up with a single value.Function
must have two arguments.
'''

def multiply(x, y):
	return x * y

p = reduce(multiply, (1, 2, 3, 4, 5))
print(p)