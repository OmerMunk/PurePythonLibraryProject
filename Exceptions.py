class LibraryExceptions(Exception):
    """A base class for all library exceptions"""
    def __init__(self, element, massage):
        self.element = element
        self.massage = massage

    def __str__(self):
        return self.massage+": "+str(self.element)


class CustomersErrors(LibraryExceptions):
    """A base class for all customers errors"""
    def __init__(self, customer_element, massage):
        self.element = customer_element
        self.massage = massage


class BooksErrors(LibraryExceptions):
    """A base class for all books errors"""
    def __init__(self, book_element, massage):
        self.element = book_element
        self.massage = massage


class LoansErrors(LibraryExceptions):
    """A base class for all loans errors"""
    def __init__(self, loan_element, massage):
        self.element = loan_element
        self.massage = massage


class UsedCustomerId(CustomersErrors):
    """This exception will raise if the user tries to add a customer with an id that is already in the database"""
    def __init__(self, customer_id):
        massage = "Customer ID already exist in the database"
        super().__init__(customer_id, massage)


class CustomerDoesntExist(CustomersErrors):
    """This exception will raise if the user tries to do an action with a customer that doesnt exist in the database"""
    def __init__(self, customer_id):
        massage = "This customer id is not in our database"
        super().__init__(customer_id, massage)


class BookValueError(BooksErrors):
    """This exception will raise if a book serial number or book id given from the user is illegal"""
    def __init__(self, serial):
        massage = "The book's serial and id need to be positive integer numbers, you entered"
        super().__init__(serial, massage)


class BookTypeError(BooksErrors):
    """This exception will raise if the user tries to add a book with a book type that is not 1, 2 or 3"""
    def __init__(self, book_type):
        massage = "Book type is not 1, 2, or 3."
        super().__init__(book_type, massage)


class BookAlreadyExist(BooksErrors):
    """This exception will raise if the user tries to add a book that already exist in the database"""
    def __init__(self, book_serial_number):
        massage = "This serial number already exist in database"
        super().__init__(book_serial_number, massage)


class BookUnavailable(BooksErrors):
    """This exception will raise if the user tries to reach a book id that doesnt exist in the database"""
    def __init__(self, book_id):
        massage = "This copy of book isn't available for loan"
        super().__init__(book_id, massage)


class SerialNumberError(BooksErrors):
    """This exception will raise if the user tries to enter a book serial number that is illegal"""
    def __init__(self, book_serial_number):
        massage = "Serial number of a book must contain only positive integer number"
        super().__init__(book_serial_number, massage)


class BookDoesntExist(BooksErrors):
    """This exception will raise if the user tries to access a book that doesnt exist in the database"""
    def __init__(self, serial):
        massage = "The book does not exist in the library"
        super().__init__(serial, massage)


class LoanDoesntExist(LoansErrors):
    """This exception will raise if the user tries to access a loan that doesnt exist in the database"""
    def __init__(self, book_id):
        massage = "This book id is not on loan"
        super().__init__(book_id, massage)


class CustomerInBlackList(CustomersErrors):
    """This exception will raise if the user tries to loan a book to a customer that is active in the black list"""
    def __init__(self, customer_id):
        massage = "This customer is in the black list, and needs to wait before loan again, customer id"
        super().__init__(customer_id, massage)


class CustomerInLateLoansList(CustomersErrors):
    """This exception will raise if the user tries to loan a book to a customer that has an unreturned book that
    its maximum return date is passed"""
    def __init__(self, customer_id):
        massage = "This customer has a book that he didn't return, and the maximum " \
                  "return date has passed, customer id"
        super().__init__(customer_id, massage)


class NonPositiveAmount(BooksErrors):
    """This exception will raise if the user tries to add copies to a book, with illegal amount"""
    def __init__(self, amount):
        massage = "Amount of copies to add must be positive, you entered"
        super().__init__(amount, massage)


class AmountValueError(BooksErrors):
    """This exception will raise if the user tries to add copies to a book, with illegal amount"""
    def __init__(self, amount):
        massage = "Amount of copies to ass must be a positive, integer number, you entered"
        super().__init__(amount, massage)


class InvalidCustomerID(CustomersErrors):
    """This exception will raise if the user tries to add a customer with an illegal ID"""
    def __init__(self, customer_id):
        massage = "This customer ID is not a legal"
        super().__init__(customer_id, massage)


class InvalidCustomerAge(CustomersErrors):
    """This exception will raise if the user tries to add a customer with an illegal age"""
    def __init__(self, age):
        massage = "This customer Age is not a legal, it must be numerical and positive"
        super().__init__(age, massage)


class InvalidYear(BooksErrors):
    """This exception will raise if the user tries to add a book with an illegal publish year"""
    def __init__(self, year):
        massage = "They year must be positive integer with 4 digits, you entered"
        super().__init__(year, massage)


class CustomerStillLoaning(CustomersErrors):
    """This exception will raise if """
    def __init__(self, name):
        massage = "This customer still has loaned books, return all the books to unregister the customer"
        super().__init__(name, massage)


class CopiesOfBookStillLoaned(BooksErrors):
    """ """
    def __init__(self, serial):
        massage = "Not possible to remove, there is copies of that book still on loan"
        super().__init__(serial, massage)
