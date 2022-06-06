from read_and_write import *
from prints import *
from Exceptions import *
import re
type_options = ['1', '2', '3']


class Books:
    def __init__(self, name, author, year_published, book_type, serial_number):
        """
        A constructor for the Books class

        :param name: The name of the book
        :param author: The name of the author of the book
        :param year_published: The publish year
        :param book_type: The book type of loan, must be 1, 2, or 3
        :param serial_number: The serial number of the product
        """
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
        self.serial_number = serial_number
        self.copies = {"available": [], "loaned": []}
        all_books.append(self)

    def remove_book(self):
        """
        This function removes a book from the database.
        Removing a book can only be done if there is no copies on loan
        """
        if len(self.copies["loaned"]) == 0:
            all_books.remove(self)
            book_removed_print(self.name)
        else:
            raise CopiesOfBookStillLoaned(self.serial_number)

    def add_book_copy(self, amount):
        """
        This function adds copies to a book in the database.

        :param amount: The amount of copies to add to a given book.
        """
        try:
            if int(amount) == float(amount):
                amount = int(amount)
            else:
                raise AmountValueError(amount)
        except ValueError:
            raise AmountValueError(amount)
        if amount > 0:
            for i in range(amount):
                self.copies["available"].append(next(new_id))  # calling the generator to generate new book ID
            add_copy_of_book_success_print(amount, self.name)
        else:
            raise NonPositiveAmount(amount)

    def __str__(self):
        """ A string representation for the Books class"""
        return f"""
        Book name:          {self.name}
        Author name:        {self.author}
        Year published:     {self.year_published} 
        Book loan type:     {self.book_type}
        Copies available:   {len(self.copies['available'])} : {self.copies['available']} 
        Copies on loan:     {len(self.copies['loaned'])} : {self.copies['loaned']}
        Serial number:      {self.serial_number}\n"""

    def __repr__(self):
        """ A collection representation for the Books class"""
        return ", "*80+str(self)


def add_book(name, author, year_published, book_type, serial_number):
    """
    This function gets data and validate if its valid before
    applying the constructor to create a new book
    """
    if book_type not in type_options:
        raise BookTypeError(book_type)
    serial_pattern = "\d+$"
    if re.match(serial_pattern, serial_number) is None:
        raise SerialNumberError(serial_number)
    for book in all_books:
        if book.serial_number == serial_number:
            raise BookAlreadyExist(serial_number)
    year_pattern = "\d{4}$"
    if re.match(year_pattern, year_published) is None:
        raise InvalidYear(year_published)
    Books(name, author, year_published, book_type, serial_number)


def find_book_by_name(book_name):
    """
    This function search for a book in the database according
    to a string given by the user representing the name of a book

        :param book_name: The string given by the user to search in the names of the books in the database
        :return: If 1 book found, returns the book. If more then 1 book found, returns a list of books with a suggestion to search again more specifically. If no books were found, returns a matching massage.
        """
    books_found = []
    for book in all_books:
        if book_name.lower() in book.name.lower():
            books_found.append(book)
    if len(books_found) == 0:
        book_not_found_print()
        return None
    elif len(books_found) == 1:
        return books_found[0]
    else:
        return list(map(lambda book: book.name, books_found))  # if several books found, displaying a short and easy to read list.


def find_book_by_serial_number(serial):
    """
        This function search for a book in the database according
        to a string given by the user representing the serial number of a book

            :param serial: The string given by the user to search in the serials of the books in the database
            :return: If 1 book found, returns the book. If more then 1 book found, returns a list of books with a suggestion to search again more specifically. If no books were found, returns a matching massage.
            """
    books_found = []
    for book in all_books:
        if serial in book.serial_number:
            books_found.append(book)
    if len(books_found) == 0:
        return None
    elif len(books_found) == 1:
        return books_found[0]
    else:
        return list(map(lambda book: (book.name, book.serial_number), books_found))  # if several books found, displaying a short and easy to read list.


def id_generator():
    """
    A generator that generate book id's, to make sure that the id will be given from the system
    and that no id will be ever repeated

    :return: A new book id each time this generator is called
    """
    book_id = last_id_given[0]+1
    while True:
        yield book_id
        book_id += 1


new_id = id_generator()


def display_all_books():
    """ Displays all the books in the database"""
    print(all_books)
