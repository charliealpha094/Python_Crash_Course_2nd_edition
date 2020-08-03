#Done by Carlos Amaral in 24/06/2020

"""
Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""

#Pizza Toppings
prompt = "\nPlease, enter a pizza topping you would like to have:"
prompt += "\n Enter 'quit' to end the program. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Ok, we'll add your requested {topping.title()} topping!")
