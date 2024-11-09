from datetime import date


class WorkExperience:
    def __init__(
        self,
        title: str,
        company: str,
        start: date,
        end: date = None
    ):
        self.title = title
        self.company = company
        self.start = start
        self.end = end
