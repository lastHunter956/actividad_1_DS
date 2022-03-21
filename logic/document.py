class Document(object):
    """
    Class used to represent an Person
    """

    def __init__(self, Id_book: int, title: str = 'Title', number_pages: int = 0, category: str = '', author: str = ''):
        """ Person constructor object.

        :param Id_book: id of person.
        :type Id_book: int
        :param title: name of book.
        :type title: str
        :param number_pages: number of pages the book.
        :type number_pages: int
        :param category: is like a kind of topic that talk the book.
        :type category: str
        :param author: name of person who writes of book.
        :type author: str
        :returns: Document object
        :rtype: object
        """
        self._Id_book = Id_book
        self._title = title
        self._number_pages = number_pages
        self._category = category
        self._author = author

    @property
    def Id_book(self) -> int:
        """ Returns id person of the Book.
          :returns: id Book.
          :rtype: int
        """
        return self._Id_book

    @Id_book.setter
    def Id_book(self, Id_book: int):
        """ The id of the book.
        :param Id_book: id of book.
        :type: int
        """
        self._Id_book = Id_book

    @property
    def title(self) -> str:
        """ Returns the name of the book.
          :returns: name of the book
          :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """ The name of the book.
        :param title: name of the book.
        :type: str
        """
        self._title = title

    @property
    def number_pages(self) -> int:
        """ Returns the number of pages the book.
          :returns: the number of pages the book.
          :rtype: int
        """
        return self._number_pages

    @number_pages.setter
    def number_pages(self, number_pages: int):
        """ the number of pages the book.
        :param number_pages: the number of pages the book.
        :type: int
        """
        self._number_pages = number_pages

    @property
    def category(self) -> str:
        """ Returns the category.
          :returns: the category.
          :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """ the category.
        :param category: is like a kind of topic that talk the book.
        :type: str
        """
        self._category = category

    @property
    def author(self) -> str:
        """ Returns the author.
          :returns: the author.
          :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author: str):
        """ the author.
        :param author: name of person who writes of book.
        :type: str
        """
        self._author = author

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4})'.format(self.Id_book, self.title, self.number_pages, self.category, self.author)

if __name__ == '__main__':
    book = Document(Id_book=73577376, title="hola ", number_pages=350, category="Novels", author="Won")
    book.title = "Almendra"
    print(book)

