# Done by Carlos Amaral in 12/06/2020

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
"""

guests = ['Rita', 'Sofia', 'Patrícia']
print(guests)

message = "Dear " + guests[0].title() + \
          " I would like to invite you for my dinner."
print(message)

message = "Dear " + guests[1].title() + \
          " I would like to invite you for my dinner."
print(message)

message = "Dear " + guests[2].title() + \
          " I would like to invite you for my dinner."
print (message)

message = "\nUnfortunatelly, " +guests[0].title() + \
          " is unable to come..."
print(message)

guests.remove('Rita')    #del(guests[1]), also works!!!
guests.insert(0, 'Madalena')
print("\n")
print(guests)

message = "Dear " + guests[0].title() + \
          " I would like to invite you for my dinner."
print(message)

message = "Dear " + guests[1].title() + \
          " I would like to invite you for my dinner."
print(message)

message = "Dear " + guests[2].title() + \
          " I would like to invite you for my dinner."
print (message)

print("\nI found a bigger Dinner table. We can have more guests.")

guests.insert(0, 'Marisa')
print(guests)

guests.insert (2, 'Lise')
print(guests)

guests.append('Isabelle')
print(guests)

message ="\nDear " + guests[0].title() + \
         " I would like to invite you for my dinner."
print(message)

message ="Dear " + guests[1].title() + \
         " I would like to invite you for my dinner."
print(message)

message = "Dear " + guests[2].title() + \
          " I would like to invite you for my dinner."
print (message)

print( "Dear "+ guests[3].title() + 
       " I would like to invite you for my dinner.")

print("Dear " + guests[4].title() + 
      " I would like to invite you for my dinner.")

print("Dear " + guests[5].title() + 
      " I would like to invite you for my dinner.")

print("\nThe table hasn't arrived yet."+ 
      " Unfortunatelly there is only space for 2 guests.")

print(guests)
popped_guests = guests.pop()
print(guests)
print(f"\nSorry, {popped_guests.title()}.")

popped_guests1 = guests.pop()
print(guests)
print(f"\nSorry, {popped_guests1.title()}...")

popped_guests2 = guests.pop()
print(guests)
print(f"\nSorry, {popped_guests2.title()}.")

popped_guests3 = guests.pop()
print(guests)
print(f"\nSorry, {popped_guests3.title()}.")

print( "Dear "+ guests[0].title() + 
       " I would like to invite you for my dinner.")
print( "Dear " + guests[1].title() + 
       " I would like to invite you for my dinner.")

del guests[0]
del guests[0]
print(guests)


