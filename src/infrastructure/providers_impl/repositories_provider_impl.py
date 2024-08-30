from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.termins_repository import TerminsRepository
from infrastructure.config.repositories_config import get_termins_repository


class RepositoriesProviderImpl(RepositoriesProvider):
    def get_termins_repository(self) -> TerminsRepository:
        return get_termins_repository()
