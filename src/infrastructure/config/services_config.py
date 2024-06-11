from application.services.termins_service import TerminsService
from infrastructure.config.providers_config import categories_of_termins_provider
from infrastructure.config.repositories_config import termins_repository, category_of_termins_repository
from infrastructure.config.translation_service_config import translation_service

termins_service = TerminsService(
    termins_repository=termins_repository,
    category_of_termins_repository=category_of_termins_repository,
    categories_of_termins_provider=categories_of_termins_provider,
    translation_service=translation_service
)
