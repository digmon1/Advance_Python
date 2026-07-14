# Parent Class 1
class Author:
    def __init__(self, author_name):
        self.__author_name = author_name

    # Getter
    def get_author_name(self):
        return self.__author_name

    # Setter
    def set_author_name(self, author_name):
        self.__author_name = author_name

    # String Method
    def __str__(self):
        return f"Author Name    : {self.__author_name}"


# Parent Class 2
class Publisher:
    def __init__(self, publisher_name):
        self.__publisher_name = publisher_name

    # Getter
    def get_publisher_name(self):
        return self.__publisher_name

    # Setter
    def set_publisher_name(self, publisher_name):
        self.__publisher_name = publisher_name

    # String Method
    def __str__(self):
        return f"Publisher Name : {self.__publisher_name}"


# Child Class
class Book(Author, Publisher):
    def __init__(self, author_name, publisher_name, book_title, price):
        Author.__init__(self, author_name)
        Publisher.__init__(self, publisher_name)
        self.__book_title = book_title
        self.__price = price

    # Getters
    def get_book_title(self):
        return self.__book_title

    def get_price(self):
        return self.__price

    # Setters
    def set_book_title(self, book_title):
        self.__book_title = book_title

    def set_price(self, price):
        self.__price = price

    # Overriding __str__()
    def __str__(self):
        return (Author.__str__(self) + "\n" +
                Publisher.__str__(self) + "\n" +
                f"Book Title     : {self.__book_title}\n"
                f"Price          : Rs.{self.__price}")


# Driver Program
book = Book(
    "James Clear",
    "Penguin Books",
    "Atomic Habits",
    1200
)

print("Book Details")
print(book)

print("\nAfter Updating Details")

book.set_book_title("Atomic Habits (2nd Edition)")
book.set_price(1500)
book.set_author_name("James Clear Updated")
book.set_publisher_name("Penguin Publications")

print(book)