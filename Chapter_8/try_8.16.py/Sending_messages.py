#Done by Carlos Amaral in 02/07/2020


import messages

text_messages = ['This is my message', 'Hello!']
sent_messages = []


messages.show_messages(text_messages)
messages.send_messages(text_messages, sent_messages)


print("\n")


from messages import show_messages

text_messages = ['This is my message', 'Hello!']
sent_messages = []

show_messages(text_messages)



print("\n\n")

from messages import show_messages as sm 

text_messages = ['This is my message', 'Hello!']
sent_messages = []


sm(text_messages)



print("\n\n")

import messages as m 

text_messages = ['This is my message', 'Hello!']
sent_messages = []

m.show_messages(text_messages)
m.send_messages(text_messages, sent_messages)


print("\n\n")


from messages import*

text_messages = ['This is my message', 'Hello!']
sent_messages = []

show_messages(text_messages)
send_messages(text_messages, sent_messages)