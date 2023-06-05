# from person import Person
# from datetime import datetime

# person1 = Person('Berke', 'Karataş', datetime(1997, 2, 1), 'Istanbul', 'B Rh+', '12345678')
# print(Person.number_of_person)
# print(Person.age_of_majority)
# print(Person.get_birth_year(person1))
# print(person1)
# print(person1.fullname)
# print(person1.email)
# print(person1.first_name)
# print(person1.last_name)
# print(person1.age)
# print(person1.birthdate) # 1997-01-02 00:00:00
# person1.birthdate = '01/02/22'
# person1.birthplace = 'Ankara'
# print(person1.blood_group)
# print(person1.identity_number)
# print(person1.is_major())
# print(person1.send_email())
# print(Person.all)
# -----------------------------------------------------------------------------------------------
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