from typing import List
from datetime import date
from data import (
    DataSource,
    PersonalInfo,
    Address,
    WorkExperience,
    Skill,
    Education)


class Demo(DataSource):
    def get_personal_info(self) -> PersonalInfo:
        return PersonalInfo("John", "Doe", date(1990, 5, 17))
    
    def get_address(self) -> Address:
        return Address("Kölner Straße", "Springfield", "51789", "DE")
    
    def get_work_experience(self) -> List[WorkExperience]:
        return [
            WorkExperience(
                "Software Engineer", "ABC Inc", date(2015, 1, 1)),
            WorkExperience(
                "Software Engineer", "DEF Inc", 
                date(2013, 1, 1), date(2015, 1, 1))
        ]
    
    def get_skills(self) -> List[Skill]:
        return [
            Skill("Python"),
            Skill("Java")
        ]
    
    def get_education(self) -> List[Education]:
        return [
            Education(
                "University of Illinois",
                "Bachelor of Science",
                date(2013, 5, 15))
        ]
    

        
