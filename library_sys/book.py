class Book:
    def __init__(self,title,author,year,available=True):
        self.title =title
        self.author =author
        self.year =year
        self.available =available


# pint information of the book
def display_info(book):
    print(f"Title: {book.title} \nAuthor: {book.author} \nYear: {book.year}")

# checking availability of the book
def check_availability(book):
        if book.available:
            print(f'{book.title} is available')
        else:
            print(f'{book.title} is not available')

# update the availability of the book
def update_availability(book, status):
        book.available = status
        if status:
            print(f"{book.title} is now available.")
        else:
            print(f"{book.title} is now unavailable.")

