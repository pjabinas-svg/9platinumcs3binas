
## Private and Public Attributes and Methods
#|Attribute| Data Type | Visibility | Why Private or Public|
#|---|---|---|---|
#|+Genre| String | Public | This is a general attribute that can be accessed from outside the class|
#|+Album| String | Public | This is a general attribute that can be accessed from outside the class|
#|+Monthly listeners| Integer | Public | This is a general attribute that can be accessed from outside the class|
#|+Name| String | Public | This is a general attribute that can be accessed from outside the class|
#|-Adress| String | Private | This is a sensitive attribute that should not be accessed from outside the class|
#|-Earnings| int | Private | This is a sensitive attribute that should not be accessed from outside the class|







class Artist:
    def __init__(self, Genre, Album, Monthly_listeners, Name, Adress, Earnings):
        self.attribute1 = Genre
        self.attribute2 = Album
        self.attribute3 = Monthly_listeners
        self.attribute4 = Name
        self.__private_attribute1 = Adress
        self.__private_attribute2 = Earnings

    def releaseAlbum(self, title):
        print(self.attribute4 + " released the album " + title)

    def releaseSong(self, title):
        print(self.attribute4 + " released the song " + title)

    def performConcert(self, play):
        if play:
            print(self.attribute4 + " is performing a concert.")
        else:
            print(self.attribute4 + " is not performing a concert.")

    def addListeners(self, amount):
        self.attribute3 += amount

    def getEarnings(self, amount):
        self.__private_attribute2 += amount 
        return self.__private_attribute2


artist1 = Artist(
    "Opm",
    "Andalucia",
    8000000,
    "IV of Spades",
    "Philippines, Manila",
    100000
)

artist2 = Artist(
    "Jazz",
    "A matter of Time",
    30000000,
    "Laufey",
    "Iceland, Reykjavik",
    21000000
)

artist1.releaseAlbum("Andalucia")
artist2.releaseAlbum("A matter of Time")

artist1.releaseSong("Kabisado")
artist2.releaseSong("Lover Girl")

artist1.performConcert(True)
artist2.performConcert(False)

artist1.addListeners(1000000)

print(artist1.getEarnings(100000))
print(artist2.getEarnings(20000000))