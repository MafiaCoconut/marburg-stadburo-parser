from abc import ABC, abstractmethod

class CategoriesOfTerminsProvider(ABC):
    @abstractmethod
    def get_adressanderung_parser_interface(self):
        pass

    @abstractmethod
    def get_eat_abholung_parser_interface(self):
        pass

    @abstractmethod
    def get_registration_office_parser_interface(self):
        pass

    @abstractmethod
    def get_others_parser_interface(self):
        pass

    @abstractmethod
    def get_auhenthaltstiteel_parser_interface(self):
        pass

