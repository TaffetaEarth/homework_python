class Reader:
    def __init__(self, n):
        self.__books = []
        self.quan = n

    def take_book(self, bookname):
        if len(self.__books) >= self.quan:
            print("Too many books already had been took")
            self.__books.append(bookname)

    def hand_over(self, bookname):
        if bookname in self.__books:
            self.__books.remove(bookname)
            print("Book", bookname, "has been returned to library")


class ChildReader(Reader):
    __books = []

    def take_book(self, bookname):
        super().take_book(bookname)


rd1 = ChildReader(1)
rd1.take_book("1984")
rd1.take_book("Harry Potter")
rd1.take_book("Lord of The Rings")
rd1.get_books()
rd1.hand_over("Harry Potter")
rd1.take_book("1984")
rd1.take_book("Lord of The Rings")
rd1.get_books()
