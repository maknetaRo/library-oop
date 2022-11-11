class Shelf():
    books = []
    def __init__(self, number, capacity):
        self.number = number 
        self.capacity = capacity 
        self.books = []

    def add_book(self, book):
        if self.capacity > len(self.books):
            self.books.append(book)
        else:
            raise Exception("You can't put a book on that shelf.")
