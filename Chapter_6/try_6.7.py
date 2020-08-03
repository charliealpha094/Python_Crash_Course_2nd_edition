#Done by Carlos Amaral in 23/06/2020

"""
Start with the program you wrote for Exercise 6-1 (page 99).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people . Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

#People

people = []
 


Patricia = {
    'first_name': 'Ana',
    'last_name': 'Soares',
    'age': '33',
    'location':'Viseu'    
    }
people.append(Patricia)

Carlos = {
    'first_name': 'Carlos',
    'last_name': 'Amaral',
    'age': '26',
    'location': 'Viseu'
    }
people.append(Carlos)

Tereza = {
    'first_name': 'Tereza',
    'last_name': 'Srbova',
    'age': '30',
    'location': 'Prague'
    }
people.append(Tereza)

for person in people:
    
    name = f"{person['first_name']} {person['last_name']}"
    age = f"{person['age']}"
    location = f"{person['location']}"

    print(f"\nName: {name.title()}")
    print(f"Age: {age.title()}")
    print(f"Location: {location.title()}")

    print(f"{name.title()}, lives in {location.title()} and is {age.title()}. ")
