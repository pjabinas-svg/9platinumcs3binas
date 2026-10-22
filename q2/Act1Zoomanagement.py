#Parent Class
class Animals:
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print(f"{self.name} makes sound.")


#Child class 1.
class Lion(Animals):
    def __init__(self, name : str):
        super().__init__(name)

    def eat(self):
        print (f"{self.name} eating Fresh meat")

    def make_sound(self):
        print (f"{self.name} roars loudly.")


#Child class 2
class Elephant(Animals):
    def __init__(self, name : str):
        super().__init__(name)

    def eat(self):
        print (f"{self.name} eating leaves.")

    def make_sound(self):
        print (f"{self.name} trumphet")

#cHILD CLSAS 3

class Monkey(Animals):
    def __init__(self, name: str):
        super().__init__(name)

    def eat(self):
        print (f"{self.name} eating banana")

    def make_sound(self):
        print(f"{self.name} chatter")

    
Lion = lion("simba")
Elephant = elephant("Dumbo")
Monkey = monkey("George")

print(Lion.make_sound())
print(Lion.eat())




print(Elephant.make_sound())
print(Elephant.eat())

print(Monkey.make_sound())
print(Monkey.eat())