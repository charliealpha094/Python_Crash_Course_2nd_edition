#Done by Carlos Amaral in 01/07/2020

"""
Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that’s being ordered. Call the function three times, using a different num-
ber of arguments each time.
"""

#Sandwiches
def make_sandwich(*items):
    """Summarize the sandwich we're going to make."""
    print("\nMaking your sandwich:")
    for item in items:
        print(f"adding- {item}...")
    print("\nYour sandwich is ready!!")

make_sandwich('meat', 'cheese', 'lettuce')
make_sandwich('mayo', 'butter')
make_sandwich('pickles', 'cucumbers')

