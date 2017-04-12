'''
Write a program that checks if the accounting equation holds true 
for any account given i.e. A = C + L.

'''
print( 'The accounting equation should always hold for any statement of account i.e: A = C +L')
print ('The calculations for a statement of financial position are generally as follows:')


assets = list(input('\n\nEnter all your Non Current Assets values: '))
NCA_total = 0
for i in assets:
	NCA_total += i
print ('NCA total = ',NCA_total)

asset2 = list(input('\n\nEnter all your Current Assets values: '))
CA_total = 0
for i in asset2:
	CA_total += i
print( 'CA total = ',CA_total)


liabilities = list(input('\n\nEnter all your Current Liabilities values: '))
CL_total = 0
for i in liabilities:
	CL_total += i
print ('CL total = ',CL_total)

net_current_assets = CA_total - CL_total
print ('\n\nThe net current assets are ',net_current_assets)

net_assets = NCA_total + net_current_assets
print( '\n\nThe net assets are ',net_assets)



capital = int(input('\n\nEnter your capital for the period: '))
print( 'Capital = ',capital)


liabilities2 = list(input('\n\nEnter all your Long Term Liabilities values: '))
LTL_total = 0
for i in liabilities2:
	LTL_total += i
print ('LTL total = ',LTL_total)

print( '\n\nVerifying the accounting equation:')

if net_assets != (capital + LTL_total):
	print ('The accounting equation has not been satisfied!\nThe accounts have not balanced!')
else:
	print ('\n\nThe accounting equation has been satisfied.\nThe accounts have balanced!')
	print ('The balancing figure stands at:\n\nNet assets = %r\nCapital + LTL = %r'%(net_assets, capital + LTL_total))

