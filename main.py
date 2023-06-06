from datetime import datetime
from person import Person
from employee import Employee, Developer, Manager

person1 = Person(
    first_name='Tony',
    last_name='Soprano',
    birthdate=datetime(1980, 4, 15),
    birthplace='New Jersey',
    blood_group='0 Rh+',
    identity_number='12345678'
)

emp1 = Employee(
    first_name='Eric',
    last_name='Murphy',
    birthdate=datetime(1993, 6, 18),
    birthplace='New York',
    blood_group='A Rh-',
    identity_number='87654321',
    salary=5000,
    company='Sbarro',
    working_days=6
)

dev1 = Developer(
    first_name='David',
    last_name='Chaum',
    birthdate=datetime(1990, 8, 12),
    birthplace='Chicago',
    blood_group='AB Rh+',
    identity_number='12378456',
    salary=7500,
    company='Nvidia',
    working_days=5,
    programming_language='Python'
)

mng1 = Manager(
    first_name='Michael',
    last_name='Scofield',
    birthdate=datetime(1985, 1, 2),
    birthplace='Chicago',
    blood_group='B Rh+',
    identity_number='11652003',
    salary=10000,
    company='Apple',
    working_days=5,
    under_employees=[emp1, dev1]
)
