from abc import ABC, abstractmethod
from .personal_info import PersonalInfo


class DataSource(ABC):
    @abstractmethod
    def get_personal_info(self) -> PersonalInfo:
        pass
