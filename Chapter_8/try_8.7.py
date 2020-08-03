#Done by Carlos Amaral in 29/06/2020

"""
Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
"""

#Album
#1st version
def make_album(artist_name, album_title):
    """Returns the name of the album and it's title."""
    album_discription = f"{artist_name}, {album_title}" 
    return album_discription.title()

album = make_album('Cocteau Twins', 'Four Calendar Cafe')
album2 = make_album('Oasis', '(Whats the story) Morning Glory?')
album3 = make_album('Portishead', 'Dummy')
print(album)
print(album2)
print(album3)


print("\n")

def make_album(artist_name, album_title, songs_number):
    """Returns the name of the album and it's title."""
    album_discription = f"{artist_name}, {album_title}, {songs_number}" 
    return album_discription.title()

album = make_album('Cocteau Twins', 'Four Calendar Cafe', '10')
album2 = make_album('Oasis', '(Whats the story) Morning Glory?', '12')
album3 = make_album('Portishead', 'Dummy', '11')
print(album)
print(album2)
print(album3)