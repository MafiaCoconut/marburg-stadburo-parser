import logging
import time

import pytest

from application.repositories.category_of_termins_repository import CategoryOfTerminsRepository
from application.repositories.termins_repository import TerminsRepository


@pytest.fixture
def termins_repository():
    return TerminsRepository()


@pytest.fixture
def category_of_termins_repository():
    return CategoryOfTerminsRepository()


@pytest.fixture
def set_category_of_termins(category_of_termins, category_of_termin_repository):
    logging.info("Тестовые категории терминов инициализированы в бд")
    for category_of_termin in category_of_termins:
        category_of_termin_repository.save(category_of_termin)

    yield

    time.sleep(3)
    category_of_termin_repository.delete_all()
    logging.info("Тестовые категории терминов удалены из бд")


@pytest.fixture
def set_termins(termins, termins_repository):
    logging.info("Тестовые термины инициализированы в бд")
    for termin in termins:
        termins_repository.save(termin)

    yield

    time.sleep(3)
    termins_repository.delete_all()
    logging.info("Тестовые термины удалены из бд")
