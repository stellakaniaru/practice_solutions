'''printing, printing'''

#assign the variable formatter four specifiers.
#at any one point,formatter should hold four items
formatter = '%r %r %r %r'

#formatter is assigned numbers to print
print formatter%(1, 2, 3, 4)

#formatter is assigned strings to print
print formatter%('one', 'two', 'three', 'four')

#formatter is assigned boolean values to print
print formatter%(True, False, True, False)

#formatter is assigned four strings to print
#each string has its own set of quotes since each is an independent entity to take up each available specifier
print formatter%(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)