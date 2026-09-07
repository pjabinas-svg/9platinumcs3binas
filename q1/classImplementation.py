
## Private and Public Attributes and Methods
#|Attribute| Data Type | Visibility | Why Private or Public|
#|--|--|--|--|--|
#|+Genre| String | Public | This is a general attribute that can be accessed from outside the class|
#|+Album| String | Public | This is a general attribute that can be accessed from outside the class|
#|+Monthly listeners| Integer | Public | This is a general attribute that can be accessed from outside the class|
#|+Name| String | Public | This is a general attribute that can be accessed from outside the class|
#|-Adress| String | Private | This is a sensitive attribute that should not be accessed from outside the class|
#|-Earnings| int | Private | This is a sensitive attribute that should not be accessed from outside the class|







class Artist:
def __init__(self, Genre, Album, Monthly listeners, Name, Adress, Earnings):
self.attribute1 = Genre
self.attribute2 = Album
self.attribute3 = Monthly listeners
self.attribute4 = Name
self.__private_attribute1 = Adress
self.___private_attribute2 = Earnings

def releaseAlbum(self, title):
        print(self.attribute4 + " released the album " + title)

def releaseSong(self, title):
        print(self.attribute4 + " released the song " + title)

def performConcert(self, play):
        if play:
            print(self.attribute4 + " is performing a concert.")
        else:
            print(self.attribute4 + " is not performing a concert.")   
