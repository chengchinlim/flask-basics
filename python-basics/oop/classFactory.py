class Book:
    types = ("hardcover", "paperback")

    def __init__(self, name, bookType):
        self.name = name
        self.type = bookType

    def __str__(self):
        return f"Name: {self.name}, BookType: {self.type}"

    @classmethod
    def createHardCoverBook(cls, name):
        return Book(name, Book.types[0])

book = Book.createHardCoverBook("Principles")
print(book)