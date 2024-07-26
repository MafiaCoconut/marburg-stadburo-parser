from infrastructure.interfaces_impl.categories_of_termins_provider_impl import CategoriesOfTerminsProviderImpl
from infrastructure.config.interfaces_config import adressanderung_parser_interface, eat_abholung_parser_interface, \
    registration_office_parser_interface, others_parser_interface, auhenthaltstiteel_parser_interface

categories_of_termins_provider = CategoriesOfTerminsProviderImpl(
    adressanderung_parser_interface=adressanderung_parser_interface,
    eat_abholung_parser_interface=eat_abholung_parser_interface,
    registration_office_parser_interface=registration_office_parser_interface,
    others_parser_interface=others_parser_interface,
    auhenthaltstiteel_parser_interface=auhenthaltstiteel_parser_interface
)

