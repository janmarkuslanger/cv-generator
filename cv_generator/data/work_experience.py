from datetime import date
from typing import Optional


class WorkExperience:
    def __init__(
        self,
        title: str,
        company: str,
        start: date,
        end: Optional[date] = None
    ):
        self.title = title
        self.company = company
        self.start = start
        self.end = end
