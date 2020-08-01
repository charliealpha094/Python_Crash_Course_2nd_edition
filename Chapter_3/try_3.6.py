#Done by Carlos Amaral in 12/06/2020



guests = ['Rita', 'Sofia', 'Patrícia']
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

message = "Unfortunatelly, " + guests[0].title() + \
          " is unable to come."
print(message)

print("\n")
guests.remove('Rita')    #del(guests[1]), also works!!!
guests.insert(0, 'Madalena')
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

print("\nI found a bigger Dinner table. We can have more guests...")
print("\n")

guests.insert(0, 'Marisa')
print(guests)

guests.insert (2, 'Lise')
print(guests)

guests.append('Isabelle')
print(guests)

message = "\nDear " + guests[0].title() + \
          " I would like to invite you for my dinner!"
print(message)

message = "Dear " + guests[1].title() + \
          " I would like to invite you for my dinner!"
print(message)

message = "Dear " + guests[2].title() + \
" I would like to invite you for my dinner!"
print (message)

print("Dear "+ guests[3].title() + 
       " I would like to invite you for my dinner.")

print("Dear " + guests[4].title() + 
      " I would like to invite you for my dinner.")

print("Dear " + guests[5].title() + 
      " I would like to invite you for my dinner.")