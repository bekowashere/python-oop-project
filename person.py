import csv
import datetime


class Person:
    number_of_person = 0
    age_of_majority = 18
    all = []

    def __init__(self, first_name: str, last_name: str, birthdate: datetime, birthplace: str, blood_group: str,
                 identity_number: str):

        assert len(identity_number) == 8, \
            f'Identity Number must consist of 8 digits. You entered: {identity_number} is {len(identity_number)} digits'

        self.first_name = first_name
        self.last_name = last_name
        self.__birthdate = birthdate
        self.__birthplace = birthplace
        self.__blood_group = blood_group
        self.__identity_number = identity_number
        self.check_unique_identity_number()

    def check_unique_identity_number(self):
        for obj in Person.all:
            if obj is not self and obj.identity_number == self.__identity_number:
                raise ValueError(f"The same identity number is used: {self.identity_number}")
        Person.all.append(self)
        Person.number_of_person += 1

    def __repr__(self):
        open_information = f"'{self.first_name}', '{self.last_name}', '{self.__birthdate}', '{self.__birthplace}'"
        secret_information = f"'{self.__blood_group}', '{self.__identity_number}'"
        return f"{self.__class__.__name__}({open_information}, {secret_information})"

    def __str__(self):
        return self.fullname

    @property
    def birthdate(self):
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, new_date):
        value = datetime.datetime.strptime(new_date, '%d/%m/%y')
        if value > datetime.datetime.today():
            raise Exception("Invalid date")
        else:
            self.__birthdate = value

    @property
    def birthplace(self):
        return self.__birthplace

    @birthplace.setter
    def birthplace(self, value):
        self.__birthplace = value

    @property
    def blood_group(self):
        return self.__blood_group

    @property
    def identity_number(self):
        return self.__identity_number

    @property
    def age(self):
        result = datetime.datetime.today().year - self.__birthdate.year
        return result

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'

    @classmethod
    def create_instance_from_csv(cls):
        with open('person.csv', 'r') as f:
            reader = csv.DictReader(f)
            csv_person = list(reader)

        for _person in csv_person:
            cls(
                first_name=_person.get('first_name'),
                last_name=_person.get('last_name'),
                birthdate=datetime.datetime.strptime(_person.get('birthdate'), '%d/%m/%y'),
                birthplace=_person.get('birthplace'),
                blood_group=_person.get('blood_group'),
                identity_number=_person.get('identity_number'),
            )

    @staticmethod
    def get_birth_year(person):
        return person.__birthdate.year

    def is_major(self):
        # self.age_of_majority ?
        if self.age >= Person.age_of_majority:
            return True
        else:
            return False

    def __connect_email(self, smtp_server):
        return f'Connecting {smtp_server}'

    def __prepare_email_body(self):
        text = f"Dear {self.fullname}\nThis is an activation email. Please click the link below."
        return text

    def send_email(self):
        self.__connect_email('Google SMTP')
        self.__prepare_email_body()
        return f'Email send successfully'
