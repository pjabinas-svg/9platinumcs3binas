class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Artist(Person):
    def __init__(self, name: str, age: int, genre: str):
        super().__init__(name, age)
        self.genre = genre
        self.songs = []
    def add_song(self, song: str):
        self.songs.append(song)

    def get_info(self):
        parentdetails = super().get_info()
        return f"{parentdetails}, Genre: {self.genre}, Songs: {', '.join(self.songs)}"

class Song:
    def __init__(self, title: str, duration: int):
        self.title = title
        self.duration = duration

    def get_info(self):
        return f"Title: {self.title}, Duration: {self.duration} seconds"

#--example code--

if __name__ == "__main__":
    print("===Test 1: INHERITANCE (Artist IS-A Person)====")
    artist1 = Artist("Blaster Silonga", 26, "OPM")
    print(f"Parent Atributes Reused from Name: {artist1.name}, Age: {artist1.age}")
    print(f"Artist Info: {artist1.get_info()}")



    print("/=== Test 2: AGGREGATION (Artist HAS-A Song) ====")
    song1 = Song("Hayy", 225)
    song2 = Song("Kabisado", 208)


    artist1.add_song(song1.title)
    artist1.add_song(song2.title)

    print(f"Song of the Artist: {artist1.get_info()}")
    for s in artist1.songs:
        print(f"Song Title: {s}")
