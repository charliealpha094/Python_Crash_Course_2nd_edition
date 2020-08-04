#Done by Carlos Amaral in 13/07/2020


#Silent cats and dogs

"""
Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
"""

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"---Printing {filename}---")

    try:
        with open(filename) as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        pass
