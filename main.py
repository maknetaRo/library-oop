from library import Library
from room import Room
from cabinet import Cabinet
from genre import Genre 
from author import Author 
from book import Book
from publisher import Publisher
from shelf import Shelf
from cabinet import Cabinet
from person import Person, Customer

def create_library():
    our_library = Library(3)
    first_room = Room("Office", 3)
    second_room = Room("Living room", 2)
    third_room = Room("Hall", 1)
    try:
        our_library.add_room(first_room)
        our_library.add_room(second_room)
        our_library.add_room(third_room)
    except Exception as error:
        print(error)
    first_cabinet = Cabinet(Genre.ROMANCE)
    first_shelf = Shelf(1,30)
    first_cabinet.add_shelf(first_shelf)
    second_cabinet = Cabinet(Genre.SELF_HELP)
    third_cabinet = Cabinet(Genre.NOVEL)
    try:
        first_room.add_cabinet(first_cabinet)
        first_room.add_cabinet(second_cabinet)
        first_room.add_cabinet(third_cabinet)
    except Exception as error:
        print(error)

    first_shelf_third_cabinet = Shelf(1, 10)
    third_cabinet.add_shelf(first_shelf_third_cabinet)

    return our_library

def create_book(author, publisher, title, genre):
    book_genre = genre
    book_author = Author(author)
    book_publisher = Publisher(publisher)

    new_book = Book(title, book_author, book_genre)
    new_book.assign_publisher(book_publisher)
  
    return new_book

def populate_library(library, books):
    for book in books:
        for cabinet in library.rooms[0].cabinets:
            if book.genre == cabinet.genre:
                cabinet.shelves[0].add_book(book)  
                print(book.genre, cabinet.genre)     
                

our_library = create_library()
book_bridgerton = create_book("Julie Quinn", "Avon", "Bridgerton: Duke and I", Genre.ROMANCE)
book_phoenix = create_book("Gene Kim", "IT Revolution Press", "The Project Phoenix", Genre.NOVEL)
book_unicorn = create_book("Gene Kim", "IT Revolution Press", "The Unicorn Project", Genre.NOVEL)
book_five_second = create_book("Mel Robbins", "Savio Republic", "The 5 Second Rule", Genre.SELF_HELP)

populate_library(our_library, [book_bridgerton, book_phoenix, book_unicorn, book_five_second])
# new_customer = Customer("John", "Doe", "01.10.2000", 1)
# try:
#     new_customer.add_rented_book(book_bridgerton)
#     new_customer.add_rented_book(book_phoenix)
#     new_customer.add_rented_book(book_unicorn)
#     new_customer.add_rented_book(book_five_second)
#     print(new_customer.number_of_rented_books())
# except Exception as error:
#     print(error)

# print(first_cabinet.shelves[0].capacity)
for room in our_library.rooms:
    print(room.name)
    for cabinet in room.cabinets:
        print(cabinet.genre)
        for shelf in cabinet.shelves:
            for book in shelf.books:
                print(book.name)