import pytest
from datetime import datetime
from domain.entities.category_of_termin import CategoryOfTermins
from domain.entities.termin import Termin

@pytest.fixture
def category_of_termins():
    return (
        [
            CategoryOfTermins(category_id=1, name="Adressanderung"),
            CategoryOfTermins(category_id=2, name="eAT abholung"),
            CategoryOfTermins(category_id=3, name="Registration office"),
            CategoryOfTermins(category_id=4, name="Others")
        ]
    )

@pytest.fixture
def termins():
    return (
        [
            Termin(category_id=1, time=datetime(year=2024, month=7, day=4, hour=16, minute=15)),
            Termin(category_id=1, time=datetime(year=2024, month=7, day=4, hour=16, minute=30)),
            Termin(category_id=1, time=datetime(year=2024, month=7, day=4, hour=16, minute=45)),
            Termin(category_id=1, time=datetime(year=2024, month=7, day=4, hour=16, minute=00)),

            Termin(category_id=2, time=datetime(year=2024, month=7, day=4, hour=16, minute=15)),
            Termin(category_id=2, time=datetime(year=2024, month=7, day=4, hour=16, minute=30)),
            Termin(category_id=2, time=datetime(year=2024, month=7, day=4, hour=16, minute=45)),
            Termin(category_id=2, time=datetime(year=2024, month=7, day=4, hour=16, minute=00)),
            Termin(category_id=2, time=datetime(year=2024, month=7, day=4, hour=17, minute=00)),

            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=16, minute=15)),
            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=16, minute=30)),
            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=16, minute=45)),
            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=16, minute=00)),
            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=17, minute=00)),
            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=17, minute=30)),

            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=16, minute=15)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=16, minute=30)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=16, minute=45)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=16, minute=00)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=18, minute=00)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=18, minute=30)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=19, minute=00)),
        ]
    )


@pytest.fixture
def termins_list(request):
    match request.param:
        case "adressanderung":
            return adressanderung_termins()
        case "eat_abholung":
            return eat_abholung_termins()
        case "registration_office":
            return registration_office_termins()
        case "others":
            return others_termins()


def adressanderung_termins():
    return (
        1,
        [
            Termin(category_id=1, time=datetime(year=2024, month=7, day=4, hour=16, minute=15)),
            Termin(category_id=1, time=datetime(year=2024, month=7, day=4, hour=16, minute=30)),
            Termin(category_id=1, time=datetime(year=2024, month=7, day=4, hour=16, minute=45)),
            Termin(category_id=1, time=datetime(year=2024, month=7, day=4, hour=16, minute=00)),
        ]
    )


def eat_abholung_termins():
    return (
        2,
        [
            Termin(category_id=2, time=datetime(year=2024, month=7, day=4, hour=16, minute=15)),
            Termin(category_id=2, time=datetime(year=2024, month=7, day=4, hour=16, minute=30)),
            Termin(category_id=2, time=datetime(year=2024, month=7, day=4, hour=16, minute=45)),
            Termin(category_id=2, time=datetime(year=2024, month=7, day=4, hour=16, minute=00)),
            Termin(category_id=2, time=datetime(year=2024, month=7, day=4, hour=17, minute=00)),
        ])


def registration_office_termins():
    return (
        3,
        [
            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=16, minute=15)),
            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=16, minute=30)),
            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=16, minute=45)),
            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=16, minute=00)),
            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=17, minute=00)),
            Termin(category_id=3, time=datetime(year=2024, month=7, day=4, hour=17, minute=30)),
        ])


def others_termins():
    return (
        4,
        [
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=16, minute=15)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=16, minute=30)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=16, minute=45)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=16, minute=00)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=18, minute=00)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=18, minute=30)),
            Termin(category_id=4, time=datetime(year=2024, month=7, day=4, hour=19, minute=00)),
        ])
