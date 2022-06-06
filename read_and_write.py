import pickle
from datetime import date, datetime
all_books = []
all_customers = []
past_customers = []
late_loans_list = []
black_list = {}
past_black_list = {}
active_loans = []
past_loans = []
last_id_given = [10000]
#  the import command for this variable is meant to be here
from global_variable import new_id


def app_launch():
    """
    This function loads all data from the file directory
    into the the program variables and database.
    In addition, it checks if a punishment of the customers
    from the black list is finished, and automatically remove them
    from the black list to the past black list
    Finally, it checks if there is a loan that
    the max return date had reached, and automatically add the loan
    to the late loans list.
    """
    try:
        pickle_in = open("all_books.pickle", "rb")
        all_books.extend(pickle.load(pickle_in))
        pickle_in.close()
    except:
        pass
    try:
        pickle_in = open("all_customers.pickle", "rb")
        all_customers.extend(pickle.load(pickle_in))
        pickle_in.close()
    except:
        pass
    try:
        pickle_in = open("past_customers.pickle", "rb")
        past_customers.extend(pickle.load(pickle_in))
        pickle_in.close()
    except:
        pass
    try:
        pickle_in = open("late_loans_list.pickle", "rb")
        late_loans_list.extend(pickle.load(pickle_in))
        pickle_in.close()
    except:
        pass
    try:
        pickle_in = open("black_list.pickle", "rb")
        black_list.update(pickle.load(pickle_in))
        pickle_in.close()
    except:
        pass
    try:
        pickle_in = open("active_loans.pickle", "rb")
        active_loans.extend(pickle.load(pickle_in))
        pickle_in.close()
    except:
        pass
    try:
        pickle_in = open("past_loans.pickle", "rb")
        past_loans.extend(pickle.load(pickle_in))
        pickle_in.close()
    except:
        pass
    try:
        global last_id_given
        txt_in = open("last_id_given", "r")
        num = int(txt_in.read())
        last_id_given.clear()
        last_id_given.append(num)
        txt_in.close()
    except:
        pass
    for customer, punishment in black_list.items():
        # for detail, day in punishment.items():
            # if date.today() > datetime.strptime(day, '%d/%m/%y').date():
                # past_black_list[customer][detail] = day
                # punishment.popitem(detail, day)
        if black_list[customer] == {}:
            black_list.pop(customer)
    for loan in active_loans:
        try:
            if date.today() > loan.max_return_date:
                if str(loan) in str(late_loans_list):
                    pass
                else:
                    late_loans_list.append(loan)
        except Exception:
            if date.today() > loan.max_return_date.date():
                if str(loan) in str(late_loans_list):
                    pass
                else:
                    late_loans_list.append(loan)


def write_files(book_list, customers_list, past_customers_list, late_loans_list,
                black_list, active_loans, past_loans, last_id_given):
    """
    This function writes all the variables and program database into files
    in the program directory, so the details can be saved for the next use
    of the program.
    """
    pickle_out = open("all_books.pickle", "wb")
    pickle.dump(book_list, pickle_out)
    pickle_out.close()

    pickle_out = open("all_customers.pickle", "wb")
    pickle.dump(customers_list, pickle_out)
    pickle_out.close()

    pickle_out = open("past_customers.pickle", "wb")
    pickle.dump(past_customers_list, pickle_out)
    pickle_out.close()

    pickle_out = open("late_loans_list.pickle", "wb")
    pickle.dump(late_loans_list, pickle_out)
    pickle_out.close()

    pickle_out = open("black_list.pickle", "wb")
    pickle.dump(black_list, pickle_out)
    pickle_out.close()

    pickle_out = open("active_loans.pickle", "wb")
    pickle.dump(active_loans, pickle_out)
    pickle_out.close()

    pickle_out = open("past_loans.pickle", "wb")
    pickle.dump(past_loans, pickle_out)
    pickle_out.close()

    # Using the generator to make sure that book id's wont be repeated
    txt_out = open("last_id_given", "w")
    txt_out.write(str(next(new_id)-1))
    txt_out.close()
