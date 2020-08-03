#Done by Carlos Amaral in 25/06/2020

"""
Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
"""


#Pizza toppings-try_7.4 (2nd Version)

prompt = "\nPlease, enter a pizza topping you would like to have: "
prompt += "\n Enter 'quit' to end the program. "

active = True
while active:
    topping = input (prompt)

    if topping == 'quit':
        active = False
    else:
        print (f"Ok, we'll add your requested {topping.title()} topping!")