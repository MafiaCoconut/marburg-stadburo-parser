import pytest

from application.services.termins_service import TerminsService
from application.services.translation_service import TranslationService


@pytest.fixture
def termins_service(termins_repository, category_of_termins_repository, categories_of_termins_provider, translation_service):
    return TerminsService(
        repositories_provider=repositories_provider,
        category_of_termins_repository=category_of_termins_repository,
        categories_of_termins_provider=categories_of_termins_provider,
        translation_service=translation_service
    )


@pytest.fixture
def translation_service():
    return TranslationService(status="Tests")