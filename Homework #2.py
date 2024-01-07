#1.1
""" This one is better:
name = input("What is your name? ")
surname = input("What is your surname? ")
print(("Your full name is " + name + " " + surname))"""
import math

first_name = 'Bohdan'
last_name = 'Popchenko'
full_name = first_name + " " + last_name
print(full_name)
#1.2
first_name = 'bohdan'
last_name = 'popchenko'
full_name = '\n' + first_name.capitalize() + " " + '\n' + last_name.capitalize()
print(full_name)
#1.3
first_name = '          Bohdan                        '
last_name = '  Popchenko           '
#full_name = first_name + " " + last_name
print('\t' + first_name.rstrip().lstrip() + '\n' + '\t' + last_name.rstrip().lstrip())

#2
radius = float(input(("What is your radius? ")))
pi = math.pi
length = 2*pi*radius
s = pi*radius**2
print(f'Your leght is {round(length,2)}.' , f'Your square is {round(s,2)}')

#3
uah_to_usd = 37.94
uah_amount = 1000
exchange = uah_amount / uah_to_usd
print(("Поточний курс складає: ") +  str(round(exchange,2)))
