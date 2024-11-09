from datetime import date


class Education:
    def __init__(
            self,
            institution: str,
            degree: str,
            graduation_date: date = None):
        self.institution = institution
        self.degree = degree
        self.graduation_date = graduation_date
