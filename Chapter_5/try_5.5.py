#Done by Carlos Amaral in 18/06/2020


"""
Turn your if - else chain from Exercise 5-4 into an if - elif -
else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.
"""


#Alien Colors 3

#(This version runs the if-elif-else chain)
alien_color = 'green'
if alien_color == 'green':
    print("Congratulations! You've earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations! You've earned 10 points!")
else:
    print("Congratulations! You've earned 15 points!")


print("\n")

alien_color = 'yellow'
if alien_color == 'green':
    print("Congratulations! You've earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations! You've earned 10 points!")
else:
    print("Congratulations! You've earned 15 points!")


print("\n")

alien_color = 'red'
if alien_color == 'green':
    print("Congratulations! You've earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations! You've earned 10 points!")
else:
    print("Congratulations! You've earned 15 points!")
