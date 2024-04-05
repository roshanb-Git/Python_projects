from library_sys.book import display_info as display_book_info
from library_sys.member import display_info as display_member_info


def borrow_book(Book, Member):
    print(f"Book: {Book.title} has been borrowed by \nMember: {Member.name}  \nMember ID: {Member.id}")


def return_book(Book, Member):
    print(f"Book: {Book.title} has been returned by \nMember: {Member.name}  \nMember ID: {Member.id}")