#Done by Carlos Amaral in 01/07/2020

"""
Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
"""

#Sending Messages
def show_messages(text_messages):
    """Prints the text messages in the list."""
    print("Showing messages:")
    for text_message in text_messages:
        print(text_message)

def send_messages(text_messages, sent_messages):
    """Prints each text message and moves each message to sent messages."""
    print("\nSending messages:")
    while text_messages:
        current_message = text_messages.pop()
        print(current_message)
        sent_messages.append(current_message)


text_messages = ['This is my 1st message', 'Hello!']
sent_messages = []

show_messages(text_messages)
send_messages(text_messages, sent_messages)

