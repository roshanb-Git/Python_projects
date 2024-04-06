from library_sys.book import Book, display_info
from library_sys.member import Member , display_info as display_member_info
from library_sys import library

# Sample books
book1 = Book("Harry Potter", "J.K. Rowling", 1997 , False )
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1990)

member1 = Member("John", "12345", active=True )
member2 = Member("Alice", "67890", active=False)


#display_info(book1)
#display_member_info(member1)

library.borrow_book(book1, member1)
library.return_book(book1, member1)

#library.borrow_book(book2, member2)  # This should fail due to member's inactive status

#library.search_book("Potter", [book1, book2])  # Searching for books containing "Potter" in title