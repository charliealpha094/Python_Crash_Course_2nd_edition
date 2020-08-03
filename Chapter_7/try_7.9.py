#Done by Carlos Amaral in 27/06/2020

"""
Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up
in finished_sandwiches .
"""

#No Pastrami

sandwich_orders = ['pastrami', 'normal chicken', 'fish', 'pastrami', 'fried egg',
                    'ham', 'pastrami']
finnished_sandwiches = []

print("Sorry, we had run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop()

    print(f"Making your sandwich: {order.title()}")
    finnished_sandwiches.append(order)

print("\nI made your sandwich: ")
for finnished_sandwich in finnished_sandwiches:
    print("* " + finnished_sandwich.title())