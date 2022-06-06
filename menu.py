from prints import*
from Customers import *
from Books import *
from Loans import *
from read_and_write import *


def app_exit():
    exit_print()
    write_files(all_books, all_customers, past_customers, late_loans_list,
                black_list, active_loans, past_loans, last_id_given)
    exit()


if __name__ == "__main__":
    welcome_print()
    app_launch()
    while True:
        main_menu_print()
        choice = input()
        while choice not in ['1', '2', '3', '4']:
            invalid_choice_print()
            main_menu_print()
            choice = input()
        if choice == '1':
            loans_menu_print()
            choice = input()
            while choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
                invalid_choice_print()
                loans_menu_print()
                choice = input()
            if choice == '1':
                customer_id, book_serial_number, book_id, loan_date = loan_action_print()
                try:
                    loan_book(customer_id, book_serial_number, book_id, loan_date)
                except CustomerInBlackList as ex:
                    print(ex)
                except CustomerInLateLoansList as ex:
                    print(ex)
                except CustomerDoesntExist as ex:
                    print(ex)
                except BookUnavailable as ex:
                    print(ex)
                except BookDoesntExist as ex:
                    print(ex)
                except BookValueError as ex:
                    print(ex)
                continue
            elif choice == '2':
                book_id, return_date = return_action_print()
                if return_date == '0':
                    try:
                        return_loan(book_id)
                    except LoanDoesntExist as ex:
                        print(ex)
                else:
                    try:
                        return_loan(book_id, return_date)
                    except LoanDoesntExist as ex:
                        print(ex)
                continue
            elif choice == '3':
                book_name = find_book_by_name_print()
                print(display_loans_by_book_name(book_name))
                continue
            elif choice == '4':
                serial_number = find_book_by_serial_print()
                print(display_loans_by_serial_number(serial_number))
                continue
            elif choice == '5':
                display_loans_by_customer(search_loan_by_customer_print())
                continue
            elif choice == '6':
                display_late_loans()
                continue
            elif choice == '7':
                display_all_loans()
                continue
            elif choice == '8':
                continue
        elif choice == '2':  # Books menu
            books_menu_print()
            choice = input()
            while choice not in ['1', '2', '3', '4', '5', '6', '7']:
                invalid_choice_print()
                books_menu_print()
                choice = input()
            if choice == '1':
                name, author, year, book_type, serial_number = add_book_print()
                try:
                    add_book(name, author, year, book_type, serial_number)
                except BookTypeError as ex:
                    print(ex)
                except BookAlreadyExist as ex:
                    print(ex)
                except SerialNumberError as ex:
                    print(ex)
                except InvalidYear as ex:
                    print(ex)
            elif choice == '2':
                serial, amount = add_copy_of_book_print()
                book = find_book_by_serial_number(serial)
                if book is None:
                    book_not_found_print()
                elif isinstance(book, list):
                    found_several_books_print(book)
                else:
                    try:
                        book.add_book_copy(amount)
                    except NonPositiveAmount as ex:
                        print(ex)
                    except AmountValueError as ex:
                        print(ex)
            elif choice == '3':
                serial_number = remove_book_print()
                book = find_book_by_serial_number(serial_number)
                if book is not None:
                    try:
                        book.remove_book()
                    except CopiesOfBookStillLoaned as ex:
                        print(ex)
            elif choice == '4':
                name = find_book_by_name_print()
                book = find_book_by_name(name)
                if book is None:
                    book_not_found_print()
                elif isinstance(book, list):
                    found_several_books_print(book)
                else:
                    book_found_print(book)
            elif choice == '5':
                serial = find_book_by_serial_print()
                book = find_book_by_serial_number(serial)
                if book is None:
                    book_not_found_print()
                elif isinstance(book, list):
                    found_several_books_print(book)
                else:
                    book_found_print(book)
            elif choice == '6':
                display_all_books()
            elif choice == '7':
                continue
        elif choice == '3':  # Customer menu
            customers_menu_print()
            choice = input()
            while choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
                invalid_choice_print()
                customers_menu_print()
                choice = input()
            if choice == '1':
                customer_id, name, city, age = register_customer_print()
                try:
                    add_customer(customer_id, name, city, age)
                except InvalidCustomerID as ex:
                    print(ex)
                except UsedCustomerId as ex:
                    print(ex)
                except InvalidCustomerAge as ex:
                    print(ex)
            elif choice == '2':
                customer = search_customer_by_id(unregister_customer())
                if isinstance(customer, Customers):
                    try:
                        customer.remove_customer()
                    except CustomerStillLoaning as ex:
                        print(ex)
                elif isinstance(customer, list):
                    found_several_costumers_print()
                    print(customer)
                else:
                    cant_find_customer_name_or_id_print()
            elif choice == '3':
                name = search_customer_by_name(search_customer_by_name_print())
                if isinstance(name, Customers) or isinstance(name, list):
                    print(name)
            elif choice == '4':
                customer_id = search_customer_by_id(search_customer_by_id_print())
                if isinstance(customer_id, Customers) or isinstance(customer_id, list):
                    print(customer_id)
            elif choice == '5':
                customer_id, new_city = change_print()
                customer = search_customer_by_id(customer_id)
                if isinstance(customer, Customers):
                    customer.change_city(new_city)
                    city_changed_print()
                    print(customer)
            elif choice == '6':
                display_black_list()
            elif choice == '7':
                display_all_customers()
            elif choice == '8':
                continue
        elif choice == '4':
            app_exit()
