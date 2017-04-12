'''
Write a program that reads in speed in m/s and
converts it to km/hr.
'''

# speed1 = input("Enter speed in m/s: ")

# speed2 = speed1 * 3.6

# print "%rm/s in km/hr is %rkm/hr"%(speed1,speed2)

def speed_in_kmhr(speed):
	new_speed = speed * 5/18
	return "speed in m/s is %r"%(new_speed)

def speed_in_ms(speed):
	new_speed = speed * 3.6
	return "Speed in km/hr is %r"%(new_speed)



