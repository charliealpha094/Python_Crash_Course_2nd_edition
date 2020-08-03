#Done by Carlos Amaral in 27/06/2020

"""
Make a list called sandwich_orders and fill it with the names of vari-
ous sandwiches. Then make an empty list called finished_sandwiches . Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
"""


#Deli

sandwich_orders = ['normal chicken', 'fish', 'fried egg', 'ham']
finnished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()

    print(f"Making your sanwich: {order.title()}")
    finnished_sandwiches.append(order)

print("\nI made your sandwich: ")
for finnished_sandwich in finnished_sandwiches:
    print("* " + finnished_sandwich.title())

