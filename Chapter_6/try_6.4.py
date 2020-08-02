#Done by Carlos Amaral in 22/06/2020

"""
Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
"""

#Glossary 2

programming_words = {
    'String': 'A sequence of characters',
    'loop': 'A loop is used for iterating over a set of statements repeatedly.',
    'comment': 'A note in source code that only the human reads.',
    'input': 'A function which lets you ask a user for some text input.',
    'dictionary': 'A collection of pair of values.',
    }

for name, meaning in programming_words.items():
    print("\n" + name.title()+ ": "  + meaning)
