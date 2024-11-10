from typing import List
from abc import ABC, abstractmethod
from .personal_info import PersonalInfo
from .address import Address
from .work_experience import WorkExperience
from .skill import Skill
from .education import Education


class DataSource(ABC):
    @abstractmethod
    def get_personal_info(self) -> PersonalInfo:
        pass

    @abstractmethod
    def get_address(self) -> Address:
        pass

    @abstractmethod
    def get_work_experience(self) -> List[WorkExperience]:
        pass

    @abstractmethod
    def get_skills(self) -> List[Skill]:
        pass

    @abstractmethod
    def get_education(self) -> List[Education]:
        pass
