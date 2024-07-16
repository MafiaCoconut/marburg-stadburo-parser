import pytest

from application.services.termins_service import TerminsService


@pytest.fixture
def termins_service(termins_repository, category_of_termins_repository, categories_of_termins_provider, translation_service):
    termins_service = TerminsService(
        termins_repository=None,
        category_of_termins_repository=None,
        categories_of_termins_provider=None,
        translation_service=None
    )