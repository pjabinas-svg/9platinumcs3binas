class Artist:
    def __init__(self, Genre, Album, Monthly_listeners, Name, Address, Earnings):
        self.genre = Genre
        self.album = Album
        self.monthly_listeners = Monthly_listeners
        self.name = Name
        self.__address = Address
        self.__earnings = Earnings
        self.songs = []

    def releaseAlbum(self, title):
        print(self.name + " released the album " + title)

    def releaseSong(self, title):
        print(self.name + " released the song " + title)

    def performConcert(self, play):
        if play:
            print(self.name + " is performing a concert.")
        else:
            print(self.name + " is not performing a concert.")

    def addListeners(self, amount):
        self.monthly_listeners += amount

    def getEarnings(self, amount):
        self.__earnings += amount
        return self.__earnings

    def addSong(self, Song):
        self.songs.append(Song)


class Song:
    def __init__(self, title, artist, genre, duration, album):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.album = album

    def displaySong(self):
        print(self.title + " - " + self.genre)


# Create instances of Artist and Song classes
Artist1 = Artist(
    "Opm",
    "Andalucia",
    8000000,
    "IV of Spades",
    "Philippines, Manila",
    100000,
)
Artist2 = Artist(
    "Jazz",
    "A matter of Time",
    30000000,
    "Laufey",
    "Iceland, Reykjavik",
    21000000,
)

# Create instances of Song class
Song1 = Song("Kabisado", "IV of Spades", "OPM", "3:45", "Andalucia")
Song2 = Song("Come Inside of My Heart", "IV of Spades", "OPM", "4:20", "CLAPCLAPCLAP")
Song3 = Song("Mundo", "IV of Spades", "OPM", "3:30", "Orange Era")

print("---before relationship---")
print(Artist1.name + " has no songs")

print()
print("---during relationship---")

print("Adding songs to " + Artist1.name + "'s collection...")
Artist1.addSong(Song1)
Artist1.addSong(Song2)
Artist1.addSong(Song3)

print("Songs published by " + Artist1.name + ":")

for song in Artist1.songs:
    song.displaySong()

print()
print("---after relationship---")
print("songs related to " + Artist1.name)

for song in Artist1.songs:
    song.displaySong()
 