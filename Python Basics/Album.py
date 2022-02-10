def make_album(artist, title):
   album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
   return album_dict

albums  = []

album = make_album('metallica', 'ride the lightning')
print(album)
albums.append(album)

album = make_album('beethoven', 'ninth symphony')
print(album)
albums.append(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)
albums.append(album)

print(albums)


