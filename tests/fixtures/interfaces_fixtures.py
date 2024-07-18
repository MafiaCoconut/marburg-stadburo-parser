import pytest

from infrastructure.interfaces_impl.adressanderung_parser_interface_impl import AdressanderungParserInterface
from infrastructure.interfaces_impl.categories_of_termins_provider_impl import CategoriesOfTerminsProviderImpl
from infrastructure.interfaces_impl.eat_abholung_parser_interface_impl import eATAbholungParserInterface
from infrastructure.interfaces_impl.others_parser_interface_impl import OthersParserInterface
from infrastructure.interfaces_impl.registration_office_parser_interface_impl import RegistrationOfficeParserInterface


@pytest.fixture
def categories_of_termins_provider(
        adressanderung_parser_interface,
        eat_abholung_parser_interface,
        registration_office_parser_interface,
        others_parser_interface
):
    return CategoriesOfTerminsProviderImpl(
        adressanderung_parser_interface=adressanderung_parser_interface,
        eat_abholung_parser_interface=eat_abholung_parser_interface,
        registration_office_parser_interface=registration_office_parser_interface,
        others_parser_interface=others_parser_interface
    )


@pytest.fixture
def adressanderung_parser_interface():
    return AdressanderungParserInterface()

@pytest.fixture
def eat_abholung_parser_interface():
    return eATAbholungParserInterface()

@pytest.fixture
def registration_office_parser_interface():
    return RegistrationOfficeParserInterface()

@pytest.fixture
def others_parser_interface():
    return OthersParserInterface()


