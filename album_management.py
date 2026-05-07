from operator import attrgetter

# Create the class, constructor and methods to create a new Email object.
class Album:
        
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist
    
    def __str__(self):
        return f"Album: {self.album_name}, Name: {self.album_artist}, Number of Songs: {self.number_of_songs}"
    
# Create list - albums1     
albums1 = []

# Add 5 Album objects and add them to the list
album1 = Album("Walk the Moon", 3, "3 Doors Down")
albums1.append(album1)

album2 = Album("Dreams are Real", 8, "Bailey Starks")
albums1.append(album2)

album3 = Album("Starry Nights", 14, "John Harper")
albums1.append(album3)

album4 = Album("Hear the Noise", 17, "Blake Hunter")
albums1.append(album4)

album5 = Album("Through the Wind", 7, "Nathan Janis")
albums1.append(album5)

# Print the list of albums1
for album in albums1:
    print(album)
    
# Sort the albums by the number of songs, ascending order
albums1.sort(key=attrgetter('number_of_songs'))
print()
# Print the sorted list of albums
for album in albums1:
    print(album)

'''Swap the element at position 1 (index 0) of albums1 with the element at 
position 2 (index 1) and print it out.
'''
print()
swap_order = [1, 0, 2, 3, 4]
album_SwapList = [albums1[i] for i in swap_order]

for album in album_SwapList:
    print(album)

# Create a new list called albums2
albums2 = []

# Add 5 album objects to the new list
album6 = Album("Name It!", 13, "Bob Dylan")
albums2.append(album6)

album7 = Album("Real World", 10, "Henry Moncleur")
albums2.append(album7)

album8 = Album("Sharing the Moments", 18, "Susan Chandler")
albums2.append(album8)

album9 = Album("Happy Days", 11, "Melinda Cherry")
albums2.append(album9)

album10 = Album("Born to Fly", 17, "Menie Chattoer")
albums2.append(album10)

# Copy the album objects from the albums1 list to the albums2 list
for album in albums1:
    albums2.append(album)
    
# Create 2 new album objects and add them to the albums2   
album11 = Album("Dark Side of the Moon", 9, "Pink Floyd")
album12 = Album("Oops! . I Did It Again", 16, "Britney Spears")
albums2.append(album11)
albums2.append(album12)

# Sort the list alphabetically
albums2.sort(key=attrgetter('album_name'))

# Print out the sorted list
print()
print("Print out the sorted list.")
for album in albums2:
    print(album)

# indices = [i for i, x in enumerate(albums2) if x == 'D']
index = next((i for i, obj in enumerate(albums2) if obj.album_name == 'Dark Side of the Moon'), -1)
print()
print("Print index of 'Dark Side of the Moon'")
print(index)

