# use Class level and static methods


from pickletools import StackObject


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods recieve a specific object instance as an argument
    # and operate on data specific to that object
    def setTitle(self, new_title):
        self.title = new_title

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print("Book Types: ", Book.getbooktypes())

# TODO: create some book instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "PAPERBACK")

# TODO: use static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1.title)
thebooks.append(b2.title)
print(thebooks)
