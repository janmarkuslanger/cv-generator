from datetime import date
from typing import Optional


class Education:
    def __init__(
            self,
            institution: str,
            degree: str,
            graduation_date: Optional[date]):
        self.institution = institution
        self.degree = degree
        self.graduation_date = graduation_date
