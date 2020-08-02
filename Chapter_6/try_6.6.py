#Done by Carlos Amaral in 23/06/2020

"""
Use the code in favorite_languages.py (page 97).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""

#Polling

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'patricia': 'c++',
    'carlos': 'c++',
    }

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

print("\n")

list = ['joana', 'tereza', 'maria', 'carlos', 'patricia']

for programmer in list:
    if programmer in favourite_languages.keys():
        print(f"\nThank you for responding the poll, {programmer.title()}.")
    else:
        print(f"{programmer.title()}, would you like to take the poll?")