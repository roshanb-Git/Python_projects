class Book:
    def __init__(self,title,author,year,category):
        self.title =title
        self.author =author
        self.year =year
        self.category =category



def display_info(Book):
    print(f"Title: {Book.title} \nAuthor: {Book.author} \nYear: {Book.year} \nCategory: {Book.category}")
