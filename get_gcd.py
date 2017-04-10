'''
Write a program to compute the GCD of two positive numbers.
'''

'''
Euclid's algorithm:
the gcd of a and b is one of the following;
the smaller value if it evenly divides the larger value,
OR
the gcd of the smaller value and the
remainder of the larger value divided by the smaller value
i.e. if a is greater than b and a is not divisible by b, then;
gcd(a,b) == gcd(b,a%b)

'''

def gcd(a, b):
	if b > a:
		if b % a == 0:
			return a
		return gcd(b % a, a)

	else:
		if a % b == 0:
			return b
		return gcd(b, a % b)

