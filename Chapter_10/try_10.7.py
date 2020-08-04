#Done by Carlos Amaral in 13/07/2020

"""
Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
"""

#Addition Calculator

print("\t --- Addition Calculator ---")

print("\n(Enter 'q' to quit)")

while True:
    x = input("\nEnter the first number: ")
    
    if x == 'q':
        break

    y = input("\nEnter the second number: ")
  
    if y == 'q':
        break

    try:
        answer = int(x) + int(y)

    except ValueError:
        print("You can only type numbers!")
    else:
        print(f"Result={answer}")

