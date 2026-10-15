class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author
     
    def display_info(self):
        print(self.title, self.author)

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages

    def display_info(self):
        print(self.title, self.author, self.number_of_pages)

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def display_info(self):
        print(self.title, self.author, self.issue_number)

#objects
pub1 = Publication("The Martian", "Andy Weir")
b1 = Book("Project Hail Mary", "Andy Weir", 460)
m1 = Magazine("National Geographic", "Various Authors", 202)

#printing the details of the objects
print("Publication Details:")
pub1.display_info()

print("\nBook Details:")
b1.display_info()

print("\nMagazine Details:")
m1.display_info()

