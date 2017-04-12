'''
The third persom singular verb form in English can be 
distinguished using the following rules:
1. If the verb ends with y, remove it and add ies.
2. If the verb ends in o, ch, s, sh, x or z, add es.
3. By default just add s.

Create a function make_3sg_form() that given a verb in 
infinitive form returns its third person singular form.
Test your function with words like: try, brush, run and fix.

Note:Regard the rules as heuristic,ie don't expect them 
to work for all cases.
Look at the string method endswith()
'''


def make_3sg_form(verb):

	#checks if the verb ends with y, removes it and replaces it with ies if it evaluates to true
	if verb.endswith('y') == True:
		return verb.replace('y', 'ies')

	#checks if the verb ends with any of the strings in the tuple and adds es if it evaluates to true
	elif verb.endswith(('o', 'ch', 's', 'sh', 'x', 'z')) == True:
		return verb + 'es'

	#adds an s to the verb if it doesnt meet any of the criteria above
	else:
		return verb + 's'			


