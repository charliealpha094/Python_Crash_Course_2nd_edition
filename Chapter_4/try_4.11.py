#Done by Carlos Amaral in 16/06/2020

"""
Start with your program from Exercise 4-1
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas .
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas .
• Prove that you have two separate lists. Print the message My favorite
pizzas are:, and then use a for loop to print the first list. Print the message
My friend’s favorite pizzas are:, and then use a for loop to print the sec-
ond list. Make sure each new pizza is stored in the appropriate list.
"""

pizzas = ['papperoni', 'neapolitan', 'margheritta', 'carbonara']
friend_pizzas = pizzas[:]
pizzas.append('sardinha')
print(pizzas)
friend_pizzas.append('canneloni')
print(friend_pizzas)

print("\nMy favourite pizzas are:")
for pizza in pizzas:
	print("* " + pizza.title())

print("\nMy friend's favourite pizzas are:")
for pizza in pizzas:
	print("* " + pizza)
