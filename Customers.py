from read_and_write import all_customers, past_customers, black_list, late_loans_list
from prints import*
import re
from Exceptions import *


class Customers:
    """A constructor for the Customers class"""
    def __init__(self, id, name, city, age):
        self.id = id
        self.name = name
        self.city = city
        self.age = age
        self.loans = {"active": [], "past": []}
        all_customers.append(self)

    def remove_customer(self):
        """This function checks if a customer has no active loans, and if so, removes it from the database"""
        if len(self.loans["active"]) == 0:
            all_customers.remove(self)
            past_customers.append(self)
        else:
            raise CustomerStillLoaning(self.name)

    def change_city(self, new_city):
        """changes a city to a customer"""
        self.city = new_city

    def __str__(self):
        """ A string representation for the Customers class"""
        return f"""
        Customer's ID:     {self.id}
        Customer's name:   {self.name}
        Customer's city:   {self.city}
        Customer's age:    {self.age}
        Active loans:      {len(self.loans['active'])}
        Past loans:        {len(self.loans['past'])}\n"""

    def __repr__(self):
        """ A collection representation for the Customers class"""
        return ", "*80+str(self)


def validate_id(customer_id):
    """This function validates if a given ID is a legal valid Israeli ID number"""
    id_pattern = "\d{9}$"
    if re.match(id_pattern, customer_id) is None:
        return "not valid id"
    id12 = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    sum_list = [int(customer_id[i]) * int(id12[i]) for i in range(9)]
    return sum(list(map(lambda x: x // 10 + x % 10, sum_list))) % 10 == 0


def add_customer(customer_id, name, city, age):
    """This function gets and validates data, and if the data is valid, applies the Customers constructor"""
    if validate_id(customer_id) is True:
        for customer in all_customers:
            if customer.id == customer_id:
                raise UsedCustomerId(customer_id)
        for customer in past_customers:
            if customer.id == customer_id:
                past_customers.remove(customer)
                all_customers.append(customer)
                customer_loaded_from_past_print()
                return None
        if age.isnumeric():
            if int(age) > 0:
                Customers(customer_id, name, city, age)
                customer_registered_print()
            else:
                raise InvalidCustomerAge(age)
        else:
            raise InvalidCustomerAge(age)
    else:
        raise InvalidCustomerID(customer_id)


def search_customer_by_name(name):
    """
    This function searches for a customer by an input given by the user representing a name of a user or a part if it

    :return: A customer if ony one had found, a list of customers if several customers contains the string, or None if no one found
    """
    search_list = []
    for customer in all_customers:
        if name.lower() in customer.name.lower():
            search_list.append(customer)
    if len(search_list) == 0:
        cant_find_customer_name_or_id_print()
        return None
    if len(search_list) == 1:
        found_customer_print()
        return search_list[0]
    else:
        found_several_costumers_print()
        return list(map(lambda x: (x.name, x.id), search_list))


def search_customer_by_id(customer_id):
    """
    This function searches for a customer by an input given by the user representing an ID of a user or a part if it

    :return: A customer if ony one had found, a list of customers if several customers contains the string, or None if no one found
    """
    search_list = []
    for customer in all_customers:
        if customer_id in customer.id:
            search_list.append(customer)
    if len(search_list) == 0:
        cant_find_customer_name_or_id_print()
        return None
    if len(search_list) == 1:
        found_customer_print()
        return search_list[0]
    else:
        found_several_costumers_print()
        return list(map(lambda x: (x.name, x.id), search_list))


def display_black_list():
    """Displays the black list, in a dictionary format: {customer ID : {Name of book that returned late : Punish end date}}"""
    print(black_list)


def display_all_customers():
    """Displays all the customers in the database"""
    print(all_customers)
