from abc import ABC, abstractmethod

class LibraryItem(ABC):

    def __init__(self, title):
        self.title = title
        self.borrowed = False

    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass


class Book(LibraryItem):

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f'"{self.title}" book borrowed successfully.')
        else:
            print(f'"{self.title}" book is already borrowed.')

    def return_item(self):
        if self.borrowed:
            self.borrowed = False
            print(f'"{self.title}" book returned successfully.')
        else:
            print(f'"{self.title}" book was not borrowed.')


class Magazine(LibraryItem):

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f'"{self.title}" magazine borrowed successfully.')
        else:
            print(f'"{self.title}" magazine is already borrowed.')

    def return_item(self):
        if self.borrowed:
            self.borrowed = False
            print(f'"{self.title}" magazine returned successfully.')
        else:
            print(f'"{self.title}" magazine was not borrowed.')


class DVD(LibraryItem):

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f'"{self.title}" DVD borrowed successfully.')
        else:
            print(f'"{self.title}" DVD is already borrowed.')

    def return_item(self):
        if self.borrowed:
            self.borrowed = False
            print(f'"{self.title}" DVD returned successfully.')
        else:
            print(f'"{self.title}" DVD was not borrowed.')


book = Book("Python Programming")
magazine = Magazine("National Geographic")
dvd = DVD("Avengers")

book.borrow()
book.borrow()
book.return_item()

print()

magazine.borrow()
magazine.return_item()

print()

dvd.borrow()
dvd.return_item()
dvd.return_item()