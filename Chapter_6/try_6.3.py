#Done by Carlos Amaral in 21/06/2020

"""
A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character ( \n ) to insert a blank line between each word-meaning
pair in your output.
"""

#Glossary

programming_words = {
    'String': 'A sequence of characters',
    'loop': 'A loop is used for iterating over a set of statements repeatedly.',
    'comment': 'A note in source code that only the human reads',
    'input': 'A function which lets you ask a user for some text input',
    'dictionary': 'A collection of pair of values',
    }

function = 'String'
print(function.title() + ":")
print(programming_words[function])

function = 'loop'
print("\n" + function.title() + ":")
print(programming_words[function])

function = 'comment'
print("\n" + function.title() + ":")
print(programming_words[function])

function = 'input'
print("\n" + function.title() + ":")
print(programming_words[function])

function = 'dictionary'
print("\n" + function.title() + ":")
print(programming_words[function])
