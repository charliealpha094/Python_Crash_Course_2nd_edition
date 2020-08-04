#Done by Carlos Amaral in 13/07/2020


#Common words


def count_common_words(filename):
    """Count the approximate number of times 'the' is repeated."""
    try:
        with open (filename, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry the {filename} you're looking for, does not exist.")
    else:
        count_word = contents.lower().count('the')
        print(f"'The' appears in {filename}, {count_word} times")

        
filename = 'Adventures_Sherlock_Holmes.txt'
count_common_words(filename)