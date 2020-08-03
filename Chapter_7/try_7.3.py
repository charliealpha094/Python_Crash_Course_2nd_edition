#Done by Carlos Amaral in 24/06/2020

"""
Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""


#Multiples of 10

number = input("Please, enter number that is multiple of 10: ")
int(number)

if  int (number) % 10 == 0:
    print(f"Congratulations!  {number} is a multiple of 10!")
else:
    print(f"Sorry,  {number} isn't a multiple of 10!")