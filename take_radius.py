'''
Write a function that takes one parameter,radius of a circle
and returns the area and perimeter of the circle.
'''

def get_radius(r):
	area = 3.142 * r * r
	perimeter = 2 * 3.142 * r
	return 'For a circle with radius {}, its area is {} and its perimeter is {}'.format(r, area, perimeter)

