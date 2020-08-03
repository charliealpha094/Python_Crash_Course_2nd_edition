#Done by Carlos Amaral in 30/06/2020

"""
Make a list containing a series of short text messages. Pass the
list to a function called show_messages() , which prints each text message.
"""


#Messages
def show_messages(text_messages):
    """Print a simple text message."""
    for message in text_messages:
        print(message)

text_messages = ['Hello, this is my message']

show_messages(text_messages)

