from typing import Optional
from datetime import date


class PersonalInfo:
    def __init__(
            self,
            firstname: str,
            lastname: str,
            birthdate: date,
            birthplace: Optional[str] = None,
            title: Optional[str] = None):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.birthplace = birthplace
        self.title = title
