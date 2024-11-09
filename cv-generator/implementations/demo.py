from datetime import date
from data import DataSource, PersonalInfo


class Demo(DataSource):
    def get_personal_info(self) -> PersonalInfo:
        return PersonalInfo("John", "Doe", date(1990, 5, 17))
        
