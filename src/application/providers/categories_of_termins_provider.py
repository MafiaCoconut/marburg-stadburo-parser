from abc import ABC, abstractmethod

from application.interfaces.parser_interface import TerminsParserInterface


class CategoriesOfTerminsProvider(ABC):
    @abstractmethod
    def get_adressanderung_parser_interface(self) -> TerminsParserInterface:
        pass

    @abstractmethod
    def get_eat_abholung_parser_interface(self) -> TerminsParserInterface:
        pass

    @abstractmethod
    def get_registration_office_parser_interface(self) -> TerminsParserInterface:
        pass

    @abstractmethod
    def get_others_parser_interface(self) -> TerminsParserInterface:
        pass

    @abstractmethod
    def get_aufenthaltstitel_parser_interface(self) -> TerminsParserInterface:
        pass

