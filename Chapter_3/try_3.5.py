#Done by Carlos Amaral in 12/06/2020

"""
You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.
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

message = "Unfortunatelly, " +guests[0].title() + \
          " is unable to come."
print(message)

guests.remove('Rita')    #del(guests[1]), also works!!!
guests.insert(0, 'Madalena')
print("\n")
print(guests)

message = "Dear " + guests[0].title() + \
          " I would like to invite you for my dinner!"
print(message)

message = "Dear " + guests[1].title() + \
          " I would like to invite you for my dinner!"
print(message)

message = "Dear " + guests[2].title() + \
          " I would like to invite you for my dinner!"
print (message)
