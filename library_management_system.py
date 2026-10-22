class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1

    def get_number_of_books(self):
        print(f"Check the lenght of list and count: {len(self.books)}")
        return self.no_of_books

    def print_all_books(self):
        if(self.no_of_books == 0):
            print("There is no books in libraray")
        else:
            print("\n--- list of libaray boos ---")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")
                print("--------------------------------------------")

lib = Library()

lib.add_book("Python Programing")
lib.add_book("Data Structure")
lib.add_book("Database System")

lib.print_all_books()
lib.get_number_of_books()