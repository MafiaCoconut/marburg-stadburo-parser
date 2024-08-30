from abc import ABC, abstractmethod

from application.repositories.termins_repository import TerminsRepository


class RepositoriesProvider(ABC):
    @abstractmethod
    def get_termins_repository(self) -> TerminsRepository:
        pass
