#Done by Carlos Amaral in 22/06/2020

"""
Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt' .
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
"""

#Rivers

rivers = {
    'Douro': 'Portugal',
    'Danube': 'Austria',
    'Tamisa': 'England',
    }

for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")
    


print("\nThe dictionary has the following rivers:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe dictionary has the following countries:")
for country in rivers.values():
    print("- " + country.title())