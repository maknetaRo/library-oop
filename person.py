class Person():
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def get_name(self):
        return self.first_name + " " + self.last_name

class Customer(Person):
    rent_books = []
    def __init__(self, first_name, last_name, date_of_birth, customer_number):
        Person.__init__(self, first_name, last_name, date_of_birth)
        self.customer_number = customer_number

    def add_rented_book(self, book):
        if len(self.rent_books) < 3:
            self.rent_books.append(book)
        else:
            raise Exception("You can't borrow more than 3 books.")
    
    def number_of_rented_books(self):
        return len(self.rent_books)

    


