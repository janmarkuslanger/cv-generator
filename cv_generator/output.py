from enum import Enum


class Language (Enum):
    ENGLISH = 'en'
    FRENCH = 'fr'
    GERMAN = 'de'
    SPANISH = 'es'
    ITALIAN = 'it'
    DUTCH = 'nl'
    PORTUGUESE = 'pt'
    POLISH = 'pl'


class Output:
    def __init__(self, language: Language):
        self.language = language