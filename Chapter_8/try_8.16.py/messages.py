#Done by Carlos Amaral in 02/07/2020


#Imports

def show_messages(text_messages):
    """Prints the text message in the list."""
    print("Showing messages:")
    for text_message in text_messages:
        print(text_message)

def send_messages(text_messages, sent_messages):
    """Prints each text message and moves each message to sent message."""
    print("\nSending messages:")
    while text_messages:
        current_message = text_messages.pop()
        print(current_message)
        sent_messages.append(current_message)