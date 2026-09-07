
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


#1. Why did you make your chosen attribute private? Explain what could go wrong if other parts of the program changed it directly.
#2. Which method changes the state of your object? Identify the attribute affected and describe what happens.
#3. How did your two objects demonstrate that instances are independent? Refer to your actual test
#output.
#4. What is the difference between your class diagram and your object diagram? Explain this using your own class.

##Answers:
#1. I made the Address and Earnings attribute private because they are sensitve and personal information about the artist. These attritubes should not be accesed or changed by other people.
#2. The addListeners method changes the state of the object because it increases the number of monthly listeners for the artist. The attribute affected is Monthly_listeners and when this method is called it adds the specified amount to the current number of listeners.
#3. The 2 objects demonstrated that the instance are independent because when I call the addListeners method to an artist object it only affects that specifict object and not the other. For example when i call to add 1,000,000 listeners to artist1 it does not affect artist number 2.                    
#4. The class diagram show the structure of the class and its attributes and methods, while the object diagram shows the specific instances of the class and their current state. In my class, the class diagram would show the Artist class with its attributes and methods, on the other hand the object diagram shows the specific isntances of the artist class and their current values for the attributes. example, artist1 has a genre of Opm, an album of Andalucia, and 8,000,000 monthly listeners, while artist2 has a genre of Jazz, an album of A matter of Time, and 30,000,000 monthly listeners.                                                           