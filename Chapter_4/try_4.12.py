#Done by Carlos Amaral in 16/06/2020

"""
All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
print("My foods are: ")
for my_food in my_foods:
	print("* " + my_food)

print("\n")

print("My favourite food is: ")
for my_food in my_foods[:1]:
    print("* " + my_food.title())

