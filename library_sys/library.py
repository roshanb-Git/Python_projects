from library_sys.book import Book, display_info ,check_availability , update_availability
from library_sys.member import Member, display_info ,check_status, update_status

# User borrow books
def borrow_book(book, member):
    if check_availability(book) and check_status(member):
        update_availability(book, False)
        print(f"{book.title} has been borrowed by \nMember: {member.name}  \nMember ID: {member.id}")

# User returns books
def return_book(book,member):
    update_availability(book,True)
    print(f"{book.title} has been returned by \nMember: {member.name}  \nMember ID: {member.id}")

# User search a book in books
def search_book(title, books):
    for book in books:
        if title.lower() in book.title.lower():
            display_info(book)