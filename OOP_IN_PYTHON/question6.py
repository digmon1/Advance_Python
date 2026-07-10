class Book:
    def __init__(self, book_id, name, author, price):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.price = price

    def display(self):
        print("\nBook Details")
        print("Book ID:", self.book_id)
        print("Book Name:", self.name)
        print("Author:", self.author)
        print("Price:", self.price)

    def update_price(self, new_price):
        self.price = new_price

    def discount(self):
        self.price = self.price * 0.90


book = Book(101, "Python Programming", "ABC", 1000)

book.display()

book.update_price(1200)

book.discount()

book.display()