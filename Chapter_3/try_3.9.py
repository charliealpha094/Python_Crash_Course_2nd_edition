#Done by Carlos Amaral in 15/06/2020

"""
Working with one of the programs from Exercises 3-4
through 3-7 (page 42), use len() to print a message indicating the number
of people you are inviting to dinner.
"""

guests = ['Rita', 'Sofia', 'Patrícia']
print(len(guests))
print(guests)

message = "Dear " + guests[0].title() + \
          " I would like to invite you for my dinner"
print(message)

message = "Dear " + guests[1].title() + \
          " I would like to invite you for my dinner"
print(message)

message = "Dear " + guests[2].title() + \
          " I would like to invite you for my dinner"
print (message)

message = "\nUnfortunatelly, " + guests[0].title() + " is unable to come"
print(message)

guests.remove('Rita')    #del(guests[1]), also works!!!
guests.insert(0, 'Madalena')
print(guests)

message = "Dear " + guests[0].title() + \
          " I would like to invite you for my dinner"
print(message)

message = "Dear " + guests[1].title() + \
          " I would like to invite you for my dinner"
print(message)

message = "Dear " + guests[2].title() + \
          " I would like to invite you for my dinner"
print (message)

print("\nI found a bigger Dinner table. We can have more guests")

guests.insert(0, 'Marisa')
print(guests)

guests.insert (2, 'Lise')
print(guests)

guests.append('Isabelle')
print(guests)

message = "\nDear " + guests[0].title() + \
          " I would like to invite you for my dinner"
print(message)

message = "Dear " + guests[1].title() + \
          " I would like to invite you for my dinner"
print(message)

message = "Dear " + guests[2].title() + \
          " I would like to invite you for my dinner"
print (message)

print( "Dear "+ guests[3].title() + 
       " I would like to invite you for my dinner")

print("Dear " + guests[4].title() + 
      " I would like to invite you for my dinner")

print("Dear " + guests[5].title() + 
      " I would like to invite you for my dinner")

print("\nThe table hasn't arrived yet." + 
      "Unfortunatelly there is only space for 2 guests")

print(guests)
popped_guests = guests.pop()
print(guests)
print(f"\nSorry, {popped_guests.title()}.")

popped_guests1 = guests.pop()
print(guests)
print(f"Sorry, {popped_guests1.title()}...")

popped_guests2 = guests.pop()
print(guests)
print(f"Sorry, {popped_guests2.title()}.")

popped_guests3 = guests.pop()
print(guests)
print(f"Sorry, {popped_guests3.title()}.")

print("\nDear " + guests[0].title() + 
      " I would like to invite you for my dinner")
print("Dear " + guests[1].title() + 
      " I would like to invite you for my dinner")

del guests[0]
del guests[0]
print(guests)
