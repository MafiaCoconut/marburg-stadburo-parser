import pytest
from datetime import datetime
from domain.entities.category_of_termin import CategoryOfTermins
from domain.entities.termin import Termin


def category_of_termins():
    return (
        [
            CategoryOfTermins(category_id=1, name="Adressanderung"),
            CategoryOfTermins(category_id=2, name="eAT abholung"),
            CategoryOfTermins(category_id=3, name="Registration office"),
            CategoryOfTermins(category_id=4, name="Others")
        ]
    )


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

