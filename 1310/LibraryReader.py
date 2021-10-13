class Reader:
    def __init__(self):
        self.__books = []

    def take_book(self, bookname):
        if len(self.__books) >= 2:
            print("Too many books already had been took")
        else:
            self.give_book(bookname)
            print("Book", bookname, "has been took, the reader has", len(self.__books), "books")

    def get_books(self):
        print(self.__books)

    def give_book(self, bookname):
        if bookname in self.__books:
            print("Book already was given")
        else:
            print("Book", bookname, "has been given")
            self.__books.append(bookname)

    def hand_over(self, bookname):
        if bookname in self.__books:
            self.__books.remove(bookname)
            print("Book", bookname, "has been returned to library")


class ChildReader(Reader):
    def take_book(self, bookname):
        if len(self.__books) >= 1:
            print("Too many books already had been took")
        else:
            super().take_book(bookname)


rd1 = ChildReader()
rd1.take_book("1984")
rd1.take_book("Harry Potter")
rd1.take_book("Lord of The Rings")
rd1.get_books()
rd1.hand_over("Harry Potter")
rd1.take_book("1984")
rd1.take_book("Lord of The Rings")
rd1.get_books()
