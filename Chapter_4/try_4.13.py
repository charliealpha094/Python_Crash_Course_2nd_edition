#Done by Carlos Amaral in 16/06/2020

"""
A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.
"""

buffet = ('sardines', 'salomon', 'shrimp', 'potatos', 'rice')
print("Our buffet: ")
for food in  buffet:
	print('* ' + food)


buffet = ('sardines', 'salomon', 'shrimp', 'kiwi', 'cake')
print("\nThe buffet has been changed: ")
for food in buffet:
	print('* ' + food)