class Person:
    #Common class for all people
    def __init__(self, firstname):
        self.firstname = firstname
class Child(Person):
    #Common class for all people
    def __init__(self, firstname):
        super().__init__(firstname)

print(Child('stupid idiot'))