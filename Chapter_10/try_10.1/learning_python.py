#Done by Carlos Amaral in 10/07/2020

"""
Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in
the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once by 
storing the lines in a list and then working with them outside the with block.
"""

#1st print: Reading an entire file.


with open ('learning_python.txt') as file_object:
    contents = file_object.read()

print(contents)




print("\n")



#2nd print: Looping over the file object

filename = 'learning_python.txt'

with open(filename) as file:
    for line in file:
        print(line.rstrip())




print("\n\n")


#3rd print: Storing the lines in a list

filename = 'learning_python.txt'

with open(filename) as x:
    lines = x.readlines()

for line in lines:
    print(line.rstrip())