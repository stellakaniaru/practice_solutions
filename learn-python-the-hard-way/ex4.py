'''names and variables'''

#number of cars
cars = 100

#space in each car
space_in_a_car = 4.0

#number of drivers
drivers = 30

#number of passengers
passengers = 90

#number of cars not driven
cars_not_driven = cars - drivers

#number of cars driven
cars_driven = drivers

#carpool capacity of the cars
carpool_capacity = cars_driven * space_in_a_car

#number of passengers per car
average_passengers_per_car = passengers / cars_driven

#print out the number of cars available
print 'There are',cars,'cars available.'

#print out number of drivers available
print 'There are only',drivers,'drivers available.'

#print out number of cars not to be driven
print 'There will be',cars_not_driven,'empty cars today.'

#print number of people to be transported
print 'We can transport',carpool_capacity,'people today.'

#print number of passengers
print 'We have',passengers,'to carpool today.'

#print number of passengers in each car
print 'We need to put about',average_passengers_per_car,'in each car.'