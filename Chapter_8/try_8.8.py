#Done by Carlos Amaral in 29/06/2020

"""
Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""

#User Albums

def make_album(artist_name, album_title):
    """Returns the name of the album and it's title."""
    album_discription = f"{artist_name}, {album_title}" 
    return album_discription.title()

while True:
    print("Please, enter the name of an artist and album")
    print("(Enter 'q' at any time to quit)")

    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break
    album_name = input("Album name: ")
    if album_name == 'q':
        break

    music = make_album(artist_name, album_name)
    print(f"\nArtist: {artist_name}, Album: {album_name} ")

print("Thanks for using our program!")