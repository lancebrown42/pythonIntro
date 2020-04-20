class Customer():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    @property
    def rentalType(self):
        return self.