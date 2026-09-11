class Artist:
    def __init__(self, Genre, Album, Monthly_listeners, Name, Address, Earnings):
        self.genre = Genre
        self.album = Album
        self.monthly_listeners = Monthly_listeners
        self.name = Name
        self.__address = Address
        self.__earnings = Earnings
        self.songs = []
        
    def addSong(self, song):
    self.songs.append(song)


class Song:
    def __init__(self, title, artist, genre, duration, album):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.album = album

    def displaySong(self):
        print(self.title + " - " + self.genre)