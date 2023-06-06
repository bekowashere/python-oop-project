from person import Person
from datetime import datetime


class Employee(Person):
    number_of_employees = 0
    all_employee = []

    raise_amount = 1.10

    daily_food_allowance = 50
    daily_carfare = 20

    pay_day = 4

    def __init__(
            self, first_name: str, last_name: str, birthdate: datetime, birthplace: str, blood_group: str,
            identity_number: str, salary: int, company: str, working_days: int = 6
    ):
        super().__init__(first_name, last_name, birthdate, birthplace, blood_group, identity_number)

        assert salary > 0, f'Salary {salary} is not greater than zero'
        assert working_days > 0, f'Working Days {working_days} is not greater than zero'
        assert working_days < 8, f'Working Days {working_days} is not smaller than eight'

        self.salary = salary
        self.company = company
        self.working_days = working_days

        Employee.all_employee.append(self)
        Employee.number_of_employees += 1

    def __repr__(self):
        # __birthdate & __identity_number -> AttributeError
        super_information = f"'{self.first_name}', '{self.last_name}', '{self.birthdate}', '{self.identity_number}'"
        class_information = f"'{self.salary}', '{self.company}'"
        return f"{self.__class__.__name__}({super_information}, {class_information})"

    @property
    def email(self):
        company_domain = self.company.strip().replace(" ", "").lower()
        return f'{self.first_name.lower()}.{self.last_name.lower()}@{company_domain}.com'

    # continue !!!
    def next_pay_day(self):
        today = datetime.today()
        _pay_day = datetime(today.year, today.month, self.pay_day)

        if _pay_day.isoweekday() < 6:
            print('weekday')
            if today > _pay_day:
                pass
        else:
            print('weekend')

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        # weekday 5=Saturday, 6=Sunday
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __calculate_carfare(self):
        weekly_expense = self.daily_carfare * self.working_days
        monthly_expense = weekly_expense * 4
        return monthly_expense

    def __calculate_food_allowance(self):
        weekly_expense = self.daily_food_allowance * self.working_days
        monthly_expense = weekly_expense * 4
        return monthly_expense

    def total_cost(self):
        # without insurance
        return self.salary + self.__calculate_carfare() + self.__calculate_food_allowance()


class Developer(Employee):
    number_of_developers = 0
    all_developers = []

    raise_amount = 1.25

    daily_food_allowance = 75
    daily_carfare = 25

    def __init__(self, first_name: str, last_name: str, birthdate: datetime, birthplace: str,
                 blood_group: str, identity_number: str, salary: int, company: str, working_days: int = 5,
                 programming_language: str = None):
        super().__init__(first_name, last_name, birthdate, birthplace, blood_group, identity_number, salary, company,
                         working_days)

        self.programming_language = programming_language

        Developer.all_developers.append(self)
        Developer.number_of_developers += 1


class Manager(Employee):
    number_of_managers = 0
    all_managers = []

    raise_amount = 1.50

    daily_food_allowance = 100
    daily_carfare = 50

    def __init__(self, first_name: str, last_name: str, birthdate: datetime, birthplace: str,
                 blood_group: str, identity_number: str, salary: int, company: str, working_days: int = 5,
                 under_employees: list = None):
        super().__init__(first_name, last_name, birthdate, birthplace, blood_group, identity_number, salary, company,
                         working_days)

        if under_employees is None:
            self.under_employees = []
        else:
            self.under_employees = under_employees

        Manager.all_managers.append(self)
        Manager.number_of_managers += 1

    def add_employee(self, emp):
        if emp not in self.under_employees:
            self.under_employees.append(emp)
            return print(f'{emp.fullname} successfully added')
        else:
            return print(f'{emp.fullname} already exists')

    def remove_employee(self, emp):
        if emp in self.under_employees:
            self.under_employees.remove(emp)
            return print(f'{emp.fullname} successfully removed')
        else:
            return print(f'{emp.fullname} does not exists')
