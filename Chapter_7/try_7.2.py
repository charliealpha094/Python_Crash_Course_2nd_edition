#Done by Carlos Amaral in 23/06/2020

"""
Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message 
saying they’ll have to wait for a table. Otherwise, report that their table is 
ready.
"""

#Restaurant seating

seating = input("How many people are in your dinner group? ")
seating = int(seating)

if seating > 8:
    print("Sorry, you'll have to wait for a table")
else:
    print("Your table is ready")