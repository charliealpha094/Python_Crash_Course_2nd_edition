#Done by Carlos Amaral in 17/06/2020

"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""

#Some tests.
wrist_watches=['casio', 'seiko', 'rolex', 'citizen']

for wrist_watch in wrist_watches:
    if wrist_watch == 'casio':
        print(wrist_watch.lower())
    else:
        print(wrist_watch.title())

print("\n")

#Inequality
requested_watch = 'seiko'

if requested_watch != 'casio':
    print("Sorry, not in our stock.")

print("\n")

#Numerical comparisions
answer = 50

if answer != 30:
    print("Your answer is incorrect. Try again, please!")


#More numercial tests
age = 16
if age < 6:
    price = 5
elif age < 18:
    price = 10
else:
    price = 15
print(f"\nYour price is {price}!")





