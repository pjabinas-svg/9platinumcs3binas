class Publication: #parent class
    def __init__(self, title, author):
        self.title = title
        self.author = author
     
    def display_info(self):
        print(self.title, self.author)

class Book(Publication): #child class
    def __init__(self, title, author, number_of_pages): 
        super().__init__(title, author) # Inheriting the attributes of the parent class
        self.number_of_pages = number_of_pages # unique attribute for Book class

    def display_info(self):
        print(self.title, self.author, self.number_of_pages)

class Magazine(Publication): #child class
    def __init__(self, title, author, issue_number):
        super().__init__(title, author) # Inheriting the attributes of the parent class
        self.issue_number = issue_number # unique attribute for Magazine class

    def display_info(self):
        print(self.title, self.author, self.issue_number)

#objects
pub1 = Publication("The Martian", "Andy Weir") # Parent class object example
b1 = Book("Project Hail Mary", "Andy Weir", 460) # Book child class object example
m1 = Magazine("National Geographic", "Various Authors", 202) # Magazine child class object example

#printing the details of the objects
print("Publication Details:") #printing the details of the parent class object
pub1.display_info() # display the information of the parent class object

print("\nBook Details:") #printing the details of the child class object
b1.display_info() # Display the information of the child class object

print("\nMagazine Details:") # printing the details of the child class object
m1.display_info() #display the information of the child class object

