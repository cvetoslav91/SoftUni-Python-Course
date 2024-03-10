from project.customer import Customer
from project.dvd import DVD

class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = [c for c in self.customers if c.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_dvd.is_rented:
            return "DVD is already rented"

        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_dvd.is_rented = True
        current_customer.rented_dvds.append(current_dvd)
        return f'{current_customer.name} has successfully rented {current_dvd.name}'

    def return_dvd(self, customer_id: int, dvd_id: int):
        current_customer = [c for c in self.customers if c.id == customer_id][0]
        try:
            searched_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        except IndexError:
            return f"{current_customer.name} does not have that DVD"

        if searched_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(searched_dvd)
            searched_dvd.is_rented = False

            return f"{current_customer.name} has successfully returned {searched_dvd.name}"

        return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for c in self.customers:
            result += f"{c}\n"
        for d in self.dvds:
            result += f"{d}\n"
        return result