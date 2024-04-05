from library_sys.book import Book
from library_sys.member import Member 
from library_sys.library import borrow_book , return_book

#Samaple usage

# Sample usage
book1 = Book("Harry Potter", "J.K. Rowling", 1997, "Fantasy")
member1 = Member("John", "12345", "123 Main St", "555-555-5555", "yj5LZ@example.com")

#display_info(book1)
#display_info(member1)

borrow_book(book1, member1)
return_book(book1, member1)