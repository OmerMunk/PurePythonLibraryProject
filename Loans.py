from read_and_write import active_loans, past_loans, all_books
from datetime import date, timedelta, datetime
from prints import *
from Exceptions import *
from Customers import *
from Books import find_book_by_serial_number


class Loans:
    def __init__(self, customer_id, customer_name, book_name, book_serial_number,
                 book_id, loan_date, loan_type, return_date=None):
        """ A constructor for the Loans class """
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.book_name = book_name
        self.book_serial_number = book_serial_number
        self.book_id = book_id
        self.loan_date = loan_date
        if loan_type == '1':
            self.max_return_date = loan_date+timedelta(days=10)
        elif loan_type == '2':
            self.max_return_date = loan_date+timedelta(days=5)
        elif loan_type == '3':
            self.max_return_date = loan_date + timedelta(days=2)
        self.return_date = return_date
        active_loans.append(self)

    def end_loan(self, return_date):
        """
        This function ends a loan.
        in addition, it removes the loan from the active loans list,
        it updates the details of the customer object according to the loans,
        and it updates the status of the book copy
        """
        if self in late_loans_list:
            late_loans_list.remove(self)
        active_loans.remove(self)
        past_loans.append(self)
        customer = search_customer_by_id(self.customer_id)
        customer.loans["active"].remove(self.book_id)
        customer.loans["past"].append(self.book_id)
        book = find_book_by_serial_number(self.book_serial_number)
        book.copies["available"].append(self.book_id)
        book.copies["loaned"].remove(self.book_id)
        try:
            if self.max_return_date < return_date.date():
                punish_date = return_date + timedelta(days=14)
                black_list.update({self.customer_id: {self.book_name: punish_date.strftime('%d/%m/%y')}})
                black_list_entry_print(self.max_return_date, punish_date)
        except Exception:
            try:
                if self.max_return_date.date() < return_date:
                    punish_date = return_date + timedelta(days=14)
                    black_list.update({self.customer_id: {self.book_name: punish_date.strftime('%d/%m/%y')}})
                    black_list_entry_print(self.max_return_date, punish_date)
            except Exception:
                if self.max_return_date < return_date:
                    punish_date = return_date + timedelta(days=14)
                    black_list.update({self.customer_id: {self.book_name: punish_date.strftime('%d/%m/%y')}})
                    black_list_entry_print(self.max_return_date, punish_date)

    def __str__(self):
        if self.return_date is None:
            return f"""
            Book name:              {self.book_name}
            Book id:                {self.book_id}
            Customer id:            {self.customer_id}
            Customer name:          {self.customer_name}
            Loan date:              {self.loan_date}
            Maximum return_date:    {self.max_return_date}
            return date :           Still on loan
            """
        else:
            return f"""
            Book name:              {self.book_name}
            Book id:                {self.book_id}
            Customer id:            {self.customer_id}
            Loan date:              {self.loan_date}
            Maximum return_date:    {self.max_return_date}
            return date :           {self.return_date}
            """

    def __repr__(self):
        return ", "*80+str(self)


def loan_book(customer_id, book_serial_number, book_id, loan_date):
    """
    This function gets and validates data, and if the data ia valid,
    applying the Loans constructor to crate a new loan.
    """
    try:
        book_id = int(book_id)
    except ValueError:
        raise BookValueError(book_id)
    if loan_date == "0":
        loan_date = date.today()
    else:
        try:
            loan_date = datetime.strptime(loan_date, '%d/%m/%y')
        except ValueError:
            invalid_date_input_print(loan_date)
            return None
    for book in all_books:
        if book_serial_number == book.serial_number:
            if book_id in book.copies["available"]:
                for customer in all_customers:
                    if customer.id == customer_id:
                        if customer.id in black_list.keys():
                            raise CustomerInBlackList(customer_id)
                        for loan in late_loans_list:
                            if loan.customer_id == customer_id:
                                raise CustomerInLateLoansList(customer_id)
                        else:
                            book_name = book.name
                            book_type = book.book_type
                            customer_name = customer.name
                            Loans(customer_id, customer_name, book_name, book_serial_number,
                                  book_id, loan_date, book_type)
                            book.copies["available"].remove(book_id)
                            book.copies["loaned"].append(book_id)
                            customer.loans["active"].append(book_id)
                            loaned_registered_print()
                            return None
                raise CustomerDoesntExist(customer_id)
            raise BookUnavailable(book_id)
    raise BookDoesntExist(book_serial_number)


def return_loan(book_id, return_date=date.today()):
    """
    This function gets and validates data, and if the data is valid
    it applies the end_loan function for the loan.
    """
    if not isinstance(return_date, date):
        try:
            return_date = datetime.strptime(return_date, '%d/%m/%y')
        except ValueError:
            invalid_date_input_print(return_date)
            return None
    for loan in active_loans:
        if str(loan.book_id) == book_id:
            loan.end_loan(return_date)
            return None
    raise LoanDoesntExist(book_id)


def display_loans_by_book_name(book_name):
    """Displays loans by book name"""
    search_list = []
    for loan in active_loans:
        if book_name in loan.book_name:
            search_list.append(loan)
    if len(search_list) > 0:
        return search_list
    else:
        no_loans_for_this_book_print(book_name)


def display_loans_by_serial_number(serial_number):
    """Displays loans by book serial number"""
    search_list = []
    for loan in active_loans:
        if serial_number in loan.book_serial_number:
            search_list.append(loan)
    if len(search_list) > 0:
        return search_list
    else:
        no_loans_for_this_book_print(serial_number)


def display_loans_by_customer(customer_id):
    """Displays loaned by customer id"""
    for loan in active_loans:
        if loan.customer_id == customer_id:
            print(loan)
            return None
    this_id_is_not_registered(customer_id)


def display_late_loans():
    """Displays all the loans that currently late to be returned"""
    print(late_loans_list)


def display_all_loans():
    """Displays all the active loans"""
    print(active_loans)
