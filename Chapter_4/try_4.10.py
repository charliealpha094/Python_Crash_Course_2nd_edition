#Done by Carlos Amaral in 16/06/2020

"""
Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Use a slice to
print three items from the middle of the list.
• Print the message The last three items in the list are:. Use a slice to print the
last three items in the list.
"""


pizzas = ['papperoni', 'neapolitan', 'margheritta', 'carbonara']
print("The first three items in the list are:")
for pizza in pizzas[:3]:   #prints the first three members
	print("* " + pizza.title())

print("\nThe items from the middle of the list are:")
for pizza in pizzas[1:3]:
	print("* " + pizza.title())

print("\nThe last three items in the list are:")
for pizza in pizzas[-3:]:
	print("* " + pizza.title())
	