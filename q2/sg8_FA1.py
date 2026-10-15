class Publication: #parent class
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def set_title(self, title):
        self.title = title
    def set_author(self, author):
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}, \nAuthor: {self.author}")

class Book(Publication): #child class
    def __init__(self, title, author, number_of_pages): 
        super().__init__(title, author) # Inheriting the attributes of the parent class
        self.number_of_pages = number_of_pages # unique attribute for Book class

    def get_number_of_pages(self):
        if self.number_of_pages < 0:
            print("Error: Number of pages cannot be negative.")
            return None
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages < 0:
            print("Error: Number of pages cannot be negative.")
        else:
            self.number_of_pages = number_of_pages
     
     
    def display_info(self):
        print(f"Title: {self.title}, \nAuthor: {self.author}, \nNumber of Pages: {self.number_of_pages}")

class Magazine(Publication): #child class
    def __init__(self, title, author, issue_number):
        super().__init__(title, author) # Inheriting the attributes of the parent class
        self.issue_number = issue_number # unique attribute for Magazine class

    def get_issue_number(self):
        return self.issue_number

    def set_issue_number(self, issue_number):
        self.issue_number = issue_number

    def display_info(self):
        print(f"Title: {self.title}, \nAuthor: {self.author}, \nIssue Number: {self.issue_number}")

#objects
pub1 = Publication("The Martian", "Andy Weir") # Parent class object example
b1 = Book("Project Hail Mary", "Andy Weir", -460) # Book child class object example
m1 = Magazine("National Geographic", "Various Authors", 202) # Magazine child class object example

#printing the details of the objects
print("Publication Details:") #printing the details of the parent class object
pub1.display_info() # display the information of the parent class object

print("\nBook Details:") #printing the details of the child class object
b1.display_info() # Display the information of the child class object

print("\nMagazine Details:") # printing the details of the child class object
m1.display_info() #display the information of the child class object

