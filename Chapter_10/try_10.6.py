#Done by Carlos Amaral in 13/07/2020

"""
One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int , you’ll get a ValueError . Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
"""


#Addition

print("Addition calculator.")

try:
  x = input("\nEnter the first number: ")
  x = int(x)

  y = input("\nEnter the second number: ")
  y = int(y)


except ValueError:
    print("Sorry, this program only accept numbers.")
else:
    sum = x + y
    print(f"Result={sum}")
