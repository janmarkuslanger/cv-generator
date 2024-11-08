from data import DataSource, PersonalInfo


class Linkedin(DataSource):
    def get_personal_info(self) -> PersonalInfo:
        return PersonalInfo("John", "Doe", "1990-01-01")
        
