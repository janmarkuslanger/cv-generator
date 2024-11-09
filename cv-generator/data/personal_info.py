from datetime import date


class PersonalInfo:
    def __init__(
            self,
            firstname: str,
            lastname: str,
            birthdate: date):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
