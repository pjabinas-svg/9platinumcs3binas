class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


class Song:
    def __init__(self, title: str, duration: int):
        self.title = title
        self.duration = duration  # duration in seconds

    def get_info(self) -> str:
        return f"'{self.title}' ({self.duration}s)"


class Artist(Person):
    def __init__(self, name: str, age: int, genre: str):
        super().__init__(name, age)
        self.genre = genre
        self.songs: list[Song] = []  # Holds Song instances (Aggregation)

    def add_song(self, song: Song):
        """Adds a Song instance to the artist's list of songs."""
        if isinstance(song, Song):
            self.songs.append(song)

    def get_info(self) -> str:
        parent_details = super().get_info()
        song_titles = ", ".join([song.title for song in self.songs]) if self.songs else "No songs added"
        return f"{parent_details}, Genre: {self.genre}, Songs: [{song_titles}]"


# ==================== EXAMPLE DEMONSTRATION    ====================

if __name__ == "__main__":
    print("=== Test 1: INHERITANCE (Artist IS-A Person) ===")
    artist1 = Artist("Blaster Silonga", 26, "OPM")
    print(f"Parent Attributes Reused -> Name: {artist1.name}, Age: {artist1.age}")
    print(f"Artist Info: {artist1.get_info()}\n")

    print("=== Test 2: AGGREGATION (Artist HAS-A Song) ===")
    song1 = Song("Hayy", 225)
    song2 = Song("Kabisado", 208)

    # Passing Song instances instead of just title strings
    artist1.add_song(song1)
    artist1.add_song(song2)

    print(f"Artist Summary: {artist1.get_info()}\n")
    print("Detailed Song List:")
    for song in artist1.songs:
        print(f" - {song.get_info()}")