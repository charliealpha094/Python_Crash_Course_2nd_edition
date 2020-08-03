#Done by Carlos Amaral in 01/07/2020

"""
Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.
"""

#Archived messages
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
send_messages(text_messages[:], sent_messages)

