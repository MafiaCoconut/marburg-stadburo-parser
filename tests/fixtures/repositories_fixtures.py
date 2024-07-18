import logging
import time

import pytest

from infrastructure.repositories_impl.category_of_termins_repositpry_impl import CategoryOfTerminsRepositoryImpl
from infrastructure.repositories_impl.termins_repository_impl import TerminsRepositoryImpl


@pytest.fixture
def termins_repository():
    return TerminsRepositoryImpl()


@pytest.fixture
def category_of_termins_repository():
    return CategoryOfTerminsRepositoryImpl()


@pytest.fixture
def set_category_of_termins(category_of_termins, category_of_termins_repository):
    logging.info("Тестовые категории терминов инициализированы в бд")
    for category_of_termin in category_of_termins:
        category_of_termins_repository.save(category_of_termin)

    yield

    # time.sleep(3)
    category_of_termins_repository.delete_all()
    logging.info("Тестовые категории терминов удалены из бд")


@pytest.fixture
def set_termins(termins, termins_repository):
    logging.info("Тестовые термины инициализированы в бд")
    for termin in termins:
        termins_repository.save(termin)

    yield

    # time.sleep(3)
    termins_repository.delete_all()
    logging.info("Тестовые термины удалены из бд")
