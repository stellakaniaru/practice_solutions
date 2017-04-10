'''
Write a program that implements the formula:
A = P * R * T
'''

principal = input('Enter principal amount: ')
rate = input('Enter rate(in percentage): ')
time = input('Enter time given(years): ')


amount = principal * rate/100 * time

print ('The amount accumulated after {} years is {}'.format(time, amount) )