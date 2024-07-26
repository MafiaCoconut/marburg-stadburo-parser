from application.providers.categories_of_termins_provider import CategoriesOfTerminsProvider
from infrastructure.interfaces_impl.adressanderung_parser_interface_impl import AdressanderungParserInterface
from infrastructure.interfaces_impl.eat_abholung_parser_interface_impl import eATAbholungParserInterface
from infrastructure.interfaces_impl.others_parser_interface_impl import OthersParserInterface
from infrastructure.interfaces_impl.registration_office_parser_interface_impl import RegistrationOfficeParserInterface
from infrastructure.interfaces_impl.aufenthaltstitel_parser_interface_impl import AufenthaltstitelParserInterface


class CategoriesOfTerminsProviderImpl(CategoriesOfTerminsProvider):
    def __init__(self,
                 adressanderung_parser_interface: AdressanderungParserInterface,
                 eat_abholung_parser_interface: eATAbholungParserInterface,
                 registration_office_parser_interface: RegistrationOfficeParserInterface,
                 others_parser_interface: OthersParserInterface,
                 auhenthaltstiteel_parser_interface: AufenthaltstitelParserInterface,
                 ):
        self.adressanderung_parser_interface = adressanderung_parser_interface
        self.eat_abholung_parser_interface = eat_abholung_parser_interface
        self.registration_office_parser_interface = registration_office_parser_interface
        self.others_parser_interface = others_parser_interface
        self.auhenthaltstiteel_parser_interface = auhenthaltstiteel_parser_interface

    def get_adressanderung_parser_interface(self):
        return self.adressanderung_parser_interface

    def get_eat_abholung_parser_interface(self):
        return self.eat_abholung_parser_interface

    def get_registration_office_parser_interface(self):
        return self.registration_office_parser_interface

    def get_others_parser_interface(self):
        return self.others_parser_interface

    def get_auhenthaltstiteel_parser_interface(self):
        return self.auhenthaltstiteel_parser_interface
