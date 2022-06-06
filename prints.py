"""Menus"""


def welcome_print():
    print("    Hello and welcome\n\n\t***REMINDER***\n\tDON'T FORGET TO CLOSE THE APPLICATION EACH TIME YOU"
          " FINISH A SEQUENCE OF ACTION/S, IN ORDER TO SAVE THE CHANGES\n\t***REMINDER***\n\n")


def main_menu_print():
    print("""    Welcome to the main menu
    To the loans menu press          1 
    To the books menu press          2 
    To the customers menu press      3 
    To exit the app press            4 """)


def loans_menu_print():
    print("""    Welcome to the loans menu
    To the make a loan press                       1 
    To return a book and finish a loan press       2 
    To display loans by book name press            3 
    To display loans by serial number press        4 
    To display loans by customer press             5 
    To display late loans press                    6 
    To display all loans press                     7 
    To go back to main menu press                  8""")


def books_menu_print():
    print("""    Welcome to the books menu
    To add a book press                             1 
    To add book copies press                        2 
    To remove a book from the library press         3 
    To find a book by it's name press               4 
    To find a book by it's serial number press      5 
    To display all books press                      6 
    To go back to main menu press                   7  """)


def customers_menu_print():
    print("""    Welcome to the customers menu
    To register a customer menu press                       1 
    To unregister a customer menu press                     2 
    To search customer by name menu press                   3 
    To search customer by id menu press                     4 
    To change a customer city press                         5 
    To display the customer's black list press              6 
    To display all the customers press                      7 
    To go back to main menu press                           8""")


def invalid_choice_print():
    print("Invalid input, try again")


def exit_print():
    print("Bye bye! see ya next time")


"""Loans"""


def loan_action_print():
    customer_id = input("Enter the customer's id")
    book_serial_number = input("Enter the book's serial number")
    book_id = input("Enter the book's id")
    loan_date = input("Enter 0 to loan now. Enter the date to loan retroactively (in the format: dd/mm/yy)")
    return customer_id, book_serial_number, book_id, loan_date


def loaned_registered_print():
    print("Loaned registered successfully ")


def return_action_print():
    book_id = input("Enter the book id")
    return_date = input("Enter the return date, make sure its in the format: dd/mm/yy,"
                        " if it's today, enter 0")
    return book_id, return_date


def no_loans_for_this_book_print(detail):
    print(f"There is no active loan with the name or id: {detail}")


def search_loan_by_customer_print():
    customer_id = input("Enter the id of the customer that you want to search his loans")
    return customer_id


def black_list_entry_print(date, punish):
    print(f"Notify the customer that tha max return date was {date},"
          f" the next time the customer can loan is after {punish}")


def invalid_date_input_print(date_value):
    print(f"The date you entered is invalid: {date_value}, you need to follow the format : dd/mm/yy")


"""Books"""


def add_book_print():
    print("Enter the name of the book")
    book_name = input()
    print("Enter the name of the author of the book")
    author_name = input()
    print("Enter the publish year")
    publish_year = input()
    print("Enter the book loan type")
    loan_type = input()
    print("Enter the book serial number")
    serial_number = input()
    return book_name, author_name, publish_year, loan_type, serial_number


def add_copy_of_book_print():
    serial = input("Enter the serial number of the book to add copies to")
    amount = input("Enter the amount of copies to add")
    return serial, amount


def remove_book_print():
    name = input("Enter the serial number of the book you want to remove")
    return name


def book_not_exist_in_library_print():
    print("This book does not exist in the library")


def book_removed_print(book_name):
    print(f"The book {book_name}, has been removed from the library, along with it's copies")


def add_copy_of_book_success_print(amount, name):
    print(f"{amount} copies have been added to the book {name}")


def find_book_by_name_print():
    name = input("Enter the name of the book(or a part of it) that you want to find")
    return name


def find_book_by_serial_print():
    serial = input("Enter the serial number of the book(or a part of it) that you want to find")
    return serial


def book_found_print(book):
    print(f"Found: {book}")


def book_not_found_print():
    print("There isn't any book that contains that name or id.")


def found_several_books_print(book):
    print(f"""Found several books that contains that name or id,
     please repeat the search with a more specific name or id
     {book}""")


"""Customers"""


def register_customer_print():
    customer_id = input("Enter the customer's ID")
    name = input("Enter the customer's name")
    city = input("Enter the customer's city")
    age = input("Enter the customer's age")
    return customer_id, name, city, age


def customer_already_exist_print():
    print("Customer ID already exist in the database")


def customer_loaded_from_past_print():
    print("Customer is a past customer, details registered as present customer")


def search_customer_by_name_print():
    name = input("Enter the name to search (or a part of it)")
    return name


def found_customer_print():
    print("Customer has found:")


def found_several_costumers_print():
    print("Found several customers with matching details, please repeat with a specific id")


def cant_find_customer_name_or_id_print():
    print("The name or id entered does not exist in the library")


def search_customer_by_id_print():
    customer_id = input("Enter the id to search (or a part of it)")
    return customer_id


def change_print():
    customer_id = input("Enter the id of the customer to change its city")
    new_city = input("Enter the new city")
    return customer_id, new_city


def city_changed_print():
    print("City has changed")


def this_id_is_not_registered(customer_it):
    print(f"This id is not registered: {customer_it}")


def unregister_customer():
    customer_id = input("Enter the ID of the customer to remove")
    return customer_id


def customer_registered_print():
    print("Customer registered successfully ")
