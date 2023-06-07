# from person import Person
# from datetime import datetime
"""
print(Person.number_of_person)  # 2
print(Employee.number_of_person)  # 2
print(Employee.number_of_employees)  # 1
print(Person.all)  # array_1
print(Employee.all)  # array_1 (same array Person.all)
print(Employee.all_employee)  # [Employee('John', 'Doe', '1993-02-01 00:00:00', '12345678', '5000', 'Paulo Factory')]
print(Employee.age_of_majority)  # 18
print(Employee.get_birth_year(emp1))  # 1993
print(emp1)  # John Doe
print(emp1.fullname)  # John Doe
print(emp1.email)  # john.doe@paulofactory.com
print(emp1.age)  # 30
print(emp1.birthdate)  # 1993-02-01 00:00:00
print(emp1.birthplace)  # NYC
emp1.birthdate = '01/02/92'
print(emp1.birthdate)  # 1992-02-01 00:00:00
emp1.birthplace = 'New York'
print(emp1.birthplace)  # New York
print(emp1.blood_group)  # B Rh+
print(emp1.identity_number)  # 12345678
print(emp1.is_major())  # True
print(emp1.send_email())  # Email send successfully

today = datetime.today()  # 2023-06-05 16:36:49.689637
print(Employee.is_workday(today))  # True

print(Employee.raise_amount)  # 1.1
print(emp1.salary)  # 5000
emp1.apply_raise()
print(emp1.salary)  # 5500

Employee.set_raise_amount(2)
print(emp1.salary)  # 5500
emp1.apply_raise()
print(emp1.salary)  # 11000

print(emp1.total_cost())  # 6680

"""

"""
date
# pay_day = 2
# datetime.datetime(2023, 12, 1)  friday -> 2023-12-04 00:00:00
# datetime.datetime(2023, 12, 2)  saturday -> 2023-12-04 00:00:00
# datetime.datetime(2023, 12, 3)  sunday -> 2023-12-04 00:00:00
# datetime.datetime(2023, 12, 4)  monday -> 2023-12-04 00:00:00
# datetime.datetime(2023, 12, 5)  tuesday -> 2024-01-02 00:00:00

# pay_day = 6
# datetime.datetime(2023, 12, 6)  wednesday -> 2023-12-06 00:00:00
# datetime.datetime(2023, 12, 7)  thursday -> 2024-01-08 00:00:00
# datetime.datetime(2023, 12, 8)  friday -> 2024-01-08 00:00:00
# datetime.datetime(2023, 12, 9)  saturday -> 2024-01-08 00:00:00
# datetime.datetime(2023, 12, 10)  sunday -> 2024-01-08 00:00:00

# pay_day = 30
# datetime.datetime(2023, 2, 10) -> ValueError: day is out of range for month

print(emp1.next_pay_day(datetime.datetime(2023, 2, 10)))
"""
